"""
Given the string representations of two integers, return the string representation of the sum of those integers.

For example:

sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

I have removed the use of BigInteger and BigDecimal in java

Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.


"""


def sum_strings(x, y):
    if not x:
        x = '0'
    if not y:
        y = '0'
    x = x.lstrip('0') or '0'
    y = y.lstrip('0') or '0'
    point_x = len(x) - 1
    point_y = len(y) - 1
    resto = 0
    res = []
    while point_x >= 0 or point_y >= 0 or resto:
        digito_x = int(x[point_x]) if point_x >= 0 else 0
        digito_y = int(y[point_y]) if point_y >= 0 else 0
        soma = digito_x + digito_y + resto
        resto = soma // 10
        res.append(str(soma % 10))
        point_x -= 1
        point_y -= 1
    resultado = ''.join(res[::-1])
    resultado = resultado.lstrip('0') or '0'

    return resultado

# Teste

print(sum_strings("123", "456"))

