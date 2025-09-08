"""
Tarefa
Escreva um metodo remainderque receba dois argumentos inteiros, dividende divisor, e retorne o resto quando o dividendo
for dividido pelo divisor. NÃO use o operador de módulo (%) para calcular o resto!

Suposição
O dividendo sempre será greater than or equal todivisor.

Notas
Certifique-se de que a remainderfunção implementada funciona exatamente da mesma forma que o Modulus operator (%).

divmodtambém foi desativado.
"""

def remainder(dividend,divisor):
	return dividend - (dividend // divisor) * divisor

# Teste

print(remainder(8,5))