"""
Ah, não, o Timmy criou um loop infinito! Ajude o Timmy a encontrar e corrigir o bug no seu loop for inacabado!
"""

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i += 1
    return res

# Teste

print(create_array(2))