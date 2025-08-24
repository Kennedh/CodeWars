"""
Complete o metodo que determinará o número mínimo de moedas necessárias para fazer troco de uma determinada quantia em
moeda americana.

As moedas utilizadas serão de meio dólar, vinte e cinco centavos, dez centavos, cinco centavos e um centavo, valendo 50
centavos, 25 centavos, 10 centavos, 5 centavos e 1 centavo, respectivamente. Elas serão representadas pelos
símbolos/sequências de caracteres H, Q, D, Ne P.

O argumento passado será um inteiro representando o valor em centavos. O valor de retorno deve ser um
hash/dicionário/objeto com os símbolos como chaves e os números de moedas como valores. Moedas não utilizadas não devem
ser incluídas no hash. Se o argumento passado for 0, o metodo deve retornar um hash vazio.
"""

def make_change(amount):
    h = amount // 50
    r = amount % 50
