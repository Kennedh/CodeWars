"""
Em uma fábrica, uma impressora imprime etiquetas para caixas.
Para um tipo de caixa, a impressora tem que usar cores que, por uma questão de simplicidade,
são nomeadas com letras de a a m.

As cores usadas pela impressora são registradas em uma string de controle.
Por exemplo, uma string de controle "boa" seria aaabbbbhaijjjm,
o que significa que a impressora usou três vezes a cor a, quatro vezes a cor b, uma vez a cor h e uma vez a cor a...

Às vezes, há problemas: falta de cores, mau funcionamento técnico e uma string de controle "ruim" é produzida,
por exemplo, aaaxbbbbyyhwawiwjjjwwm com letras que não vão de a a m.

Você tem que escrever uma função printer_error que, dada uma string,
retornará a taxa de erro da impressora como uma string representando um racional cujo numerador é o número de erros e o
denominador o comprimento da string de controle. Não reduza essa fração a uma expressão mais simples.

A string tem um comprimento maior ou igual a um e contém apenas letras de a a z.
"""

def printer_error(s):
    pass


palavra = "Kennedh"
print(len(palavra))