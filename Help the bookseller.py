"""
Um livreiro tem muitos livros classificados em 26 categorias rotuladas A, B, C, ..., Z.
Cada livro tem um código de pelo menos 3 caracteres.
O primeiro caractere de um código é uma letra maiúscula que define a categoria do livro .

No estoque do livreiro, cada código é seguido por um espaço e por um número inteiro positivo,
que indica a quantidade de livros desse código em estoque.

Tarefa
Você receberá a lista de estoque do livreiro e uma lista de categorias.
Sua tarefa é encontrar o número total de livros na lista de estoque do livreiro,
com os códigos das categorias na lista de categorias. Observação: os códigos estão na mesma ordem em ambas as listas.

Retorne o resultado como uma string descrita no exemplo abaixo,
ou como uma lista de pares (Haskell/Clojure/Racket/Prolog).

Se alguma das listas de entrada estiver vazia, retornar uma string vazia
ou uma matriz/lista vazia (Clojure/Racket/Prolog).
"""

def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
    statu = {}
    for item in stocklist:
        parts = item.split()
        if len(parts) != 2:
            continue
        code, quantity = parts[0], parts[1]
        letter = code[0]
        statu[letter] = statu.get(letter, 0) + int(quantity)

    res_parts = [f"({t} : {statu.get(t, 0)})" for t in categories]
    return " - ".join(res_parts)


# Teste

b = ["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
c = ["A", "B", "C", "W"]

print(stock_list(b,c))