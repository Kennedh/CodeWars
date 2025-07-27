"""
Não me dê cinco!
Neste kata, você obtém o número inicial e o número final de uma região e deve retornar a contagem de todos os números,
exceto aqueles com 5. Os números inicial e final são inclusivos!
"""

def dont_give_me_five(start,end):
    res = 0
    for n in range(start,end + 1):
        if "5" not in str(n):
            res += 1
    return res

# Teste

print(dont_give_me_five(1,9))