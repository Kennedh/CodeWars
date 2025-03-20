"""
O relógio mostra h horas, m minutos e s segundos depois da meia-noite.

Sua tarefa é escrever uma função que retorna o tempo desde a meia-noite em milissegundos.

1 segundo = 1000 milissegundos
1 minuto = 60000 milissegundos
1 hora = 3600000 milissegundos
"""

def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)

# Teste

print(past(0,1,1))
print(past(1,1,1))
print(past(0,0,0))
print(past(1,0,1))
print(past(1,0,0))
