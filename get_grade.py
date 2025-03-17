"""
Complete a função para que ela encontre a média das três notas passadas a ela e retorne o valor da letra associado a essa nota.

Pontuação numérica Letra Nota
90 <= pontuação <= 100 'A'
80 <= pontuação < 90 'B'
70 <= pontuação < 80 'C'
60 <= pontuação < 70 'D'
0 <= pontuação < 60 'F'
Os valores testados estão todos entre 0 e 100.
Não há necessidade de verificar valores negativos ou valores maiores que 100.
"""

def get_grade(s1, s2, s3):
    g = (s1 + s2 + s3) / 3
    if (g >= 90) and (g <= 100):
        return "A"
    elif (g >= 80) and (g <= 90):
        return "B"
    elif (g >= 70) and (g <= 80):
        return "C"
    elif (g >= 60) and (g <= 70):
        return "D"
    elif g < 60:
        return "F"

# Teste

print(get_grade(95, 90, 93))
print(get_grade(80, 85, 96))
print(get_grade(60, 70, 80))
print(get_grade(52, 65, 20))