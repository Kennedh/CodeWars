#Escreva uma função que aceite uma matriz de 10 números inteiros (entre 0 e 9)
#e que retorne uma sequência desses números no formato de um número de telefone.

#Então tem que retornar: (123) 456-7890

def create_phone_number(n):
    return f"({str(n[0])+str(n[1])+str(n[2])}) {str(n[3])+str(n[4])+str(n[5])}-{str(n[6])+str(n[7])+str(n[8])+str(n[9])}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# 05/05/2025 Treinando desafios feitos a uns certo tempo sem olhar como tinha feito antes

def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"