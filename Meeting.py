"""
John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result
between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)
(TORNBULL, BJON)"
It can happen that in two distinct families with the same family name two people have the same first name too.

Notes
You can see another examples in the "Sample tests".

"""

def meeting(s):
    s = s.upper()
    convidados = s.split(';')
    convidados_separados = []

    for convidado in convidados:
        nome, sobrenome = convidado.split(':')
        convidados_separados.append((nome, sobrenome))
    convidados_ordenados = sorted(convidados_separados, key=lambda x: (x[1], x[0]))

    res = ''
    for nome, sobrenome in convidados_ordenados:
        res += f'({sobrenome}, {nome})'
    return res

# Teste

print(meeting("Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"))

