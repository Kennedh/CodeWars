"""
Dada uma sequência de números inteiros, conte quantas vezes esse número inteiro se repete e, em seguida, retorne
uma sequência mostrando a contagem e o número inteiro.

Exemplo:"1123"

Aqui 1 vem duas vezes então <count><integer>será"21"
então 2 vem uma vez então <count><integer>será"12"
então 3 vem uma vez então <count><integer>será"13"
portanto a string de saída será "211213".

Da mesma forma "211213"retornará "1221121113" (1 vez 2, 2 vezes 1, 1 vez 2, 1 vez 1, 1 vez 3)

Retornar ""para strings vazias, nulas ou não numéricas


"""

def count_me(sequence):
    if not sequence or not sequence.isdigit():
        return ""
    result = []
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:
            result.append(str(count))
            result.append(sequence[i - 1])
            count = 1
    result.append(str(count))
    result.append(sequence[-1])

    return ''.join(result)

# teste

print(count_me('12322212223443'))
