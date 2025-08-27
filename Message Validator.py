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
import re

def is_a_valid_message(msg):
    parts = re.findall(r'\d+|[a-zA-Z]+', msg)
    for i in range(0, len(parts), 2):
        if i+1 >= len(parts):
            return False
        num = int(parts[i])
        word = parts[i+1]
        if len(word) != num:
            return False
    return True