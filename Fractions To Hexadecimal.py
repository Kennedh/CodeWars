"""
Suppose I want to change the improper fraction 41/4 to hexadecimal. The decimal equivalent of 41/4 is 10.25. The
integer part is easy: 10 = a (hexadecimal). The fractional part is 0.25 = 1/4 = 4/16. But the first place to the
right of the hexadecimal point in base 16 is 16ths place. So 41/4 = 10 4/16 = a.4 in hexadecimal.

Write a function f2hex() that takes a non-negative fraction in string form and converts it to hexadecimal. Carry your
answer out to six hexadecimal places but remove trailing zeroes and trailing hexadecimal points.

Examples
f2hex('1/2') → '0.8'
f2hex('3/4') → '0.c'
f2hex('88/1') → '58'
f2hex('99/98') → '1.029cbc'
f2hex('7/7') → '1'
"""


def f2hex(fraction):
    num, den = map(int, fraction.split('/'))
    integer_part = num // den
    fractional_part = num / den - integer_part

    if integer_part == 0:
        hex_integer = '0'
    else:
        hex_integer = hex(integer_part)[2:].lower()

    hex_fractional = ''
    remaining = fractional_part

    for _ in range(6):
        remaining *= 16
        digit = int(remaining)
        hex_fractional += hex(digit)[2:].lower()
        remaining -= digit
        if remaining == 0:
            break

    hex_fractional = hex_fractional.rstrip('0')
    if hex_fractional:
        return f"{hex_integer}.{hex_fractional}"
    else:
        return hex_integer

# Teste

print(f2hex('43967/434758'))
print(f2hex('265373/56'))
print(f2hex('2/216679'))
print(f2hex('701334/806'))
print(f2hex('7997476/8891'))
print(f2hex('92/589298'))
print(f2hex('588/948'))
print(f2hex('5305972/995'))