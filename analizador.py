#!/usr/bin/env python3

def analizar_bloque(hex_input):
    # Limpiar y convertir a bytes
    hex_clean = hex_input.replace(" ", "").replace("0x", "")
    b = bytes.fromhex(hex_clean)

    print(f"\n🔎 Análisis de: {hex_input}")
    print("-" * 40)
    print(f"Hex limpio       : {hex_clean.upper()}")
    print(f"Bytes            : {b}")
    print(f"Número decimal   : {int.from_bytes(b, 'big')}")
    print(f"Número decimal (little-endian): {int.from_bytes(b, 'little')}")
    print(f"Binario          : {bin(int.from_bytes(b, 'big'))[2:].zfill(len(b)*8)}")

    try:
        ascii_str = b.decode("ascii")
        print(f"ASCII (directo)  : {ascii_str}")
    except UnicodeDecodeError:
        print("ASCII (directo)  : no legible")

    print(f"Bytes invertidos : {b[::-1]}")
    try:
        ascii_inv = b[::-1].decode("ascii")
        print(f"ASCII invertido  : {ascii_inv}")
    except UnicodeDecodeError:
        print("ASCII invertido  : no legible")
    print("-" * 40)

# Puedes cambiar esta línea para probar otros bloques
if __name__ == "__main__":
    bloque = input("Introduce el bloque hex (ej: 04 3B E6 51): ")
    analizar_bloque(bloque)
