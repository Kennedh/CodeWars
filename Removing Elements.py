"""
Pegue um array e remova cada segundo elemento do array.
Sempre mantenha o primeiro elemento e comece a remover com o próximo elemento.
"""

def remove_every_other(my_list):
    return my_list[::2]

# Teste

print(remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep"]))