"""
Complete o método que recebe um valor booleano e retorna uma string "Sim" para verdadeiro,
ou uma string "Não" para falso.
"""

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Teste

print(bool_to_word(True))
print(bool_to_word(False))