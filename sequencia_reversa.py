"""
Faça uma função que retorne uma lista de inteiros de N ao 1 onde n>0
"""

def reverse_seq(n):
    arr = [num for num in range(n,0,-1)]
    return arr

# Teste

print(reverse_seq(5))
print(reverse_seq(4932))
print(reverse_seq(6922))