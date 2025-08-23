"""
Escreva uma função que receba um inteiro não negativo (segundos) como entrada e retorne o tempo em um formato
legível por humanos ( HH:MM:SS)

HH= horas, preenchidas com 2 dígitos, intervalo: 00 - 99
MM= minutos, preenchidos com 2 dígitos, intervalo: 00 - 59
SS= segundos, preenchidos com 2 dígitos, intervalo: 00 - 59
O tempo máximo nunca ultrapassa 359999 ( 99:59:59)

Você pode encontrar alguns exemplos nos acessórios de teste.
"""

def make_readable(seconds):
    h = seconds // 3600
    r = seconds % 3600
    m = r // 60
    s = r % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

# Teste

print(make_readable(3599))