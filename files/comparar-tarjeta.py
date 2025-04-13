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

def comparar(p1, p2):
    todas = sorted(set(p1.keys()) | set(p2.keys()))
    for pagina in todas:
        val1 = p1.get(pagina, '---- ---- ---- ----')
        val2 = p2.get(pagina, '---- ---- ---- ----')
        estado = "✅" if val1 == val2 else "❌"
        print(f"Página {pagina:2}: {val1} vs {val2}   {estado}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 comparar_tarjetas.py tarjeta1.txt tarjeta2.txt")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f1, open(sys.argv[2], 'r') as f2:
        contenido1 = f1.read()
        contenido2 = f2.read()

    paginas1 = extraer_paginas(contenido1)
    paginas2 = extraer_paginas(contenido2)

    comparar(paginas1, paginas2)
