"""
Os caixas eletrônicos permitem códigos PIN de 4 ou 6 dígitos,
e os códigos PIN não podem conter nada além de exatamente 4 ou exatamente 6 dígitos.

Se a função receber uma string PIN válida, retorne true, caso contrário, retorne false.
"""

def validate_pin(pin):
    res = None
    if len(pin) == 4 or len(pin) == 6:
        for l in pin:
            if not l.isdigit():
                return False
            else:
                res = True
    else:
        return False
    return res

# Teste

print(validate_pin("1234g6"))