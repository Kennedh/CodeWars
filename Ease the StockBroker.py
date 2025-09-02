"""
Os clientes colocam ordens para uma corretora na forma de sequências de caracteres. A ordem pode ser simples, múltipla
ou vazia.

Tipo de uma ordem simples: Cotação/espaço em branco/Quantidade/espaço em branco/Preço/espaço em branco/Status

onde Quote é formado por um caractere sem espaço em branco, Quantity é um int, Price é um double (com ponto decimal
obrigatório "." ), Status é representado pela letra B (comprar) ou pela letra S (vender).

Exemplo:
"GOOG 300 542.0 B"

Uma ordem múltipla é a concatenação de ordens simples com uma vírgula entre cada uma.

Exemplo:
"ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"

ou

"ZNGA 1300 2.66 B,CLH15.NYM 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B"

Para facilitar ao corretor da bolsa, sua tarefa é produzir uma sequência de tipos

"Buy: b Sell: s" onde b e s são formatados 'duplo' sem decimal, b representando o preço total das ações compradas e s o
preço total das ações vendidas.

Exemplo:
"Buy: 294990 Sell: 0"

Infelizmente, às vezes os clientes cometem erros. Ao encontrar erros nos pedidos, você deve identificar esses pedidos
malformados e gerar uma sequência de caracteres do tipo:

"Buy: b Sell: s; Badly formed nb: badly-formed 1st simple order ;badly-formed nth simple order ;"

onde nb é o número de ordens simples mal formadas, b representa o preço total de ações compradas com ordem simples
correta e s o preço total de ações vendidas com ordem simples correta.

Exemplos:
"Buy: 263 Sell: 11802; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;"

"Buy: 100 Sell: 56041; Badly formed 1: ZNGA 1300 2.66 ;"

Notas:
Se a ordem estiver vazia, Comprar é 0 e Vender é 0, portanto o retorno é: "Comprar: 0 Vender: 0".
Devido ao Codewars, as diferenças de espaço em branco nem sempre aparecerão nos resultados dos testes.
Com Golang (e talvez outros) você pode usar um formato com "%.0f" para "Comprar" e "Vender".
"""


def balance_statement(lst):
    if not lst:
        return "Buy: 0 Sell: 0"
    bad_orders = []
    sell = 0.0
    buy = 0.0

    for order in lst.split(","):
        order = order.strip()
        parts = order.split()

        try:
            quote = parts[0]

            if "." in parts[1]:
                raise ValueError("Quantidade não pode ter ponto decimal")
            quantity = int(parts[1])

            if "." not in parts[2]:
                raise ValueError("Preço precisa ter ponto decimal")
            price = float(parts[2])

            status = parts[3].upper()

            if status == "B":
                buy += quantity * price
            elif status == "S":
                sell += quantity * price
            else:
                bad_orders.append(order)

        except (IndexError, ValueError):
            bad_orders.append(order)

    if not bad_orders:
        return f"Buy: {buy:.0f} Sell: {sell:.0f}"
    else:
        bf = f"Badly formed {len(bad_orders)}: "
        bf += " ;".join(bad_orders) + " ;"
        return f"Buy: {buy:.0f} Sell: {sell:.0f}; {bf}"


# Teste

print(balance_statement("ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"))


















