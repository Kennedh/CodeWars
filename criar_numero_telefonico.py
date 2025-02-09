#Escreva uma função que aceite uma matriz de 10 números inteiros (entre 0 e 9)
#e que retorne uma sequência desses números no formato de um número de telefone.

#Eu gostaria de fazer nos moldes brasileiros mas para dar certo tem que ser validado no CodeWars
#Então tem que retornar: (123) 456-7890

def create_phone_number(n):
    return f"({str(n[0])+str(n[1])+str(n[2])}) {str(n[3])+str(n[4])+str(n[5])}-{str(n[6])+str(n[7])+str(n[8])+str(n[9])}"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
