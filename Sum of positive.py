"""
Você obtém uma matriz de números e retorna a soma de todos os positivos.
Se não houver nada para somar, a soma padrão é 0.
"""

def positive_sum(arr):
    res = 0
    if not arr:
        return 0
    else:
        for num in arr:
            if num <= 0:
                num = 0
            else:
                res += num
    return res

# Teste

print(positive_sum([1,2,3,4,5])) # 15
print(positive_sum([1,-2,3,4,5])) # 13
print(positive_sum([-1,2,3,4,-5])) # 9