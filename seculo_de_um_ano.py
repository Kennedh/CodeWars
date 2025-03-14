"""
O primeiro século abrange do ano 1 até e incluindo o ano 100, o segundo século - do ano 101 até e incluindo o ano 200, etc.

Tarefa
Dado um ano, retorne o século em que ele está.
"""

def century(year):
    return int(year / 100) if year % 100 == 0 else int(year / 100 + 1)

# Teste

print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))
print(century(356))