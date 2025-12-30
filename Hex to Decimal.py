"""
Complete the function which converts hex number (given as a string) to a decimal number.
"""

def hex_to_dec(s):
    try:
        return int(s,16)
    except ValueError:
        return "Não é decimal"

# Teste

print(hex_to_dec("1A3"))
print(hex_to_dec("Gato"))