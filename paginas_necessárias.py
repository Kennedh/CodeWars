"""
Seus colegas pediram para você copiar alguns papéis para eles. Você sabe que há 'n' colegas e os papéis têm 'm' páginas.

Sua tarefa é calcular quantas páginas em branco você precisa. Se n < 0 ou m < 0, retorne 0.
"""

def paperwork(n, m):
    r = n * m
    if m < 0 or n < 0:
        r = 0
    return r

# Test

print(paperwork(2,5))
print(paperwork(-2,5))
print(paperwork(5,-5))