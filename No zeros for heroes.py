"""
Números terminados em zero são chatos.

Elas podem ser divertidas no seu mundo, mas não aqui.

Livre-se deles. Só dos que estão no fim.
"""

def no_boring_zeros(n):
    res = str(n)[-1::-1]
    res = res.replace("-", "")
    return int(str(int(res))[-1::-1]) if n > 0 else -int(str(int(res))[-1::-1])

# Teste

print(no_boring_zeros(6464400))
print(no_boring_zeros(100))
print(no_boring_zeros(400000))
