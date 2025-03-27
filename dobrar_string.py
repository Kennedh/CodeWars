"""
Dada uma string, você deve retornar uma string na qual cada caractere (diferenciando maiúsculas de minúsculas)
seja repetido uma vez.
"""

def double_char(s):
    db_str = ""
    for st in s:
        db_str += st
        db_str += st
    return db_str

# Teste

print(double_char("AbCd"))