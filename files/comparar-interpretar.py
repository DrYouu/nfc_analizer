import re
import sys

def extraer_paginas(contenido):
    paginas = {}
    for linea in contenido.splitlines():
        match = re.match(r'Page (\d+): ([0-9A-Fa-f]{2} [0-9A-Fa-f]{2} [0-9A-Fa-f]{2} [0-9A-Fa-f]{2})', linea)
        if match:
            pagina = int(match.group(1))
            datos = match.group(2).upper()
            paginas[pagina] = datos
    return paginas

def interpretar(datos_hex):
    bytes_list = datos_hex.split()
    interpretaciones = []

    # Intentar como ASCII
    try:
        ascii_str = ''.join(chr(int(b, 16)) if 32 <= int(b, 16) <= 126 else '.' for b in bytes_list)
        if any(c.isalnum() for c in ascii_str):
            interpretaciones.append(f"ASCII: {ascii_str}")
    except:
        pass

    # Detectar patrones comunes
    if all(b == 'FF' for b in bytes_list):
        interpretaciones.append("Relleno (FF FF FF FF)")
    elif all(b == '00' for b in bytes_list):
        interpretaciones.append("Vacío (00 00 00 00)")

    # Interpretar como valor numérico
    try:
        valor_decimal = int(''.join(bytes_list), 16)
        interpretaciones.append(f"Decimal: {valor_decimal}")
    except:
        pass

    return "; ".join(interpretaciones) if interpretaciones else "Sin interpretación clara"

def comparar(p1, p2):
    todas = sorted(set(p1.keys()) | set(p2.keys()))
    for pagina in todas:
        val1 = p1.get(pagina, '---- ---- ---- ----')
        val2 = p2.get(pagina, '---- ---- ---- ----')
        if val1 == val2:
            print(f"Página {pagina:2}: {val1} ✅")
        else:
            print(f"Página {pagina:2}:")
            print(f"  → A: {val1} | {interpretar(val1)}")
            print(f"  → B: {val2} | {interpretar(val2)}")
            print("")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 comparar_interpretar.py tarjeta1.txt tarjeta2.txt")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f1, open(sys.argv[2], 'r') as f2:
        contenido1 = f1.read()
        contenido2 = f2.read()

    paginas1 = extraer_paginas(contenido1)
    paginas2 = extraer_paginas(contenido2)

    comparar(paginas1, paginas2)
