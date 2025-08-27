"""
Neste kata, você tem uma string de entrada e deve verificar se ela é uma mensagem válida. Para decidir isso, você
precisa dividir a string pelos números e, em seguida, comparar os números com o número de caracteres na substring seguinte.

Por exemplo, "3hey5hello2hi"deve ser dividido em 3, hey, 5, hello, 2, hie a função deve retornar true, porque "hey"tem
3 caracteres, "hello"tem 5 e "hi"tem 2; como os números e as contagens de caracteres correspondem, o resultado é true.

Notas:

As mensagens são compostas apenas de letras e dígitos
Os números podem ter vários dígitos: por exemplo, "4code13hellocodewars"é uma mensagem válida
Cada número deve corresponder ao número de caracteres na substring a seguir, caso contrário a mensagem será inválida:
por exemplo "hello5", e "2hi2"são inválidos
Se a mensagem for uma string vazia, você deve retornartrue
"""

def is_a_valid_message(msg):
    i = 0

    while i < len(msg):
        if not msg[i].isdigit():
            return False

        num = 0
        while i < len(msg) and msg[i].isdigit():
            num = num * 10 + int(msg[i])
            i += 1

        word = msg[i: i + num]
        if len(word) != num:
            return False
        i += num
    return True

# Teste

print(is_a_valid_message("3hey5hello2hi"))