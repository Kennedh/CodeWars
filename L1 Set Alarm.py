"""
Escreva uma função chamada setAlarm/set_alarm/set-alarm/setalarm (dependendo do idioma) que receba dois parâmetros.
O primeiro parâmetro, employed, é true sempre que você estiver empregado e o segundo parâmetro,
vacation, é true sempre que você estiver de férias.

A função deve retornar true se você estiver empregado
e não de férias (porque essas são as circunstâncias sob as quais você precisa definir um alarme).
"""

def set_alarm(employed, vacation):
    return employed is True and vacation is False

# Teste

print(set_alarm(True, True))
print(set_alarm(False, True))
print(set_alarm(False, False))
print(set_alarm(True, False))