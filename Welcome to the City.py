"""
Crie um método que receba como entrada o nome, a cidade e o estado para dar as boas-vindas a uma pessoa.
Observe que nameserá um array composto por um ou mais valores que devem ser unidos com um espaço entre cada um,
e o comprimento do namearray em casos de teste pode variar.
"""

def say_hello(name, city, state):
    return f'Hello, {" ".join(name)}! Welcome to {city}, {state}!'

# Teste

print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona'))