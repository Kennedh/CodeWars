"""
Dado um mês como um inteiro de 1 a 12, retorne a qual trimestre do ano ele pertence como um número inteiro.

Por exemplo: mês 2 (fevereiro), faz parte do primeiro trimestre; mês 6 (junho), faz parte do segundo trimestre;
e mês 11 (novembro), faz parte do quarto trimestre.
"""

def quarter_of(month):
    if month <= 3:
        return 1
    elif month <= 6:
        return 2
    elif month <= 9:
        return 3
    elif month <= 12:
        return 4
