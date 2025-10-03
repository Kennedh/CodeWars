"""Sua tarefa para completar este Kata é escrever uma função que formate uma duração, fornecida como um número de
segundos, de uma forma amigável.

A função deve aceitar um número inteiro não negativo. Se for zero, ela retorna apenas "now". Caso contrário, a duração
é expressa como uma combinação de years, days, hourse .minutesseconds

Fica muito mais fácil entender com um exemplo:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
Para o propósito deste Kata, um ano tem 365 dias e um dia tem 24 horas.

Observe que os espaços são importantes.

Regras detalhadas
A expressão resultante é composta por componentes como 4 seconds, 1 year, etc. Em geral, um número inteiro positivo e
uma das unidades de tempo válidas, separados por um espaço. A unidade de tempo é usada no plural se o número inteiro
for maior que 1.

Os componentes são separados por uma vírgula e um espaço ( ", "). Exceto o último componente, que é separado por
" and ", assim como seria escrito em inglês.

Uma unidade de tempo mais significativa ocorrerá antes de uma menos significativa. Portanto, 1 second and 1 yearnão
está correto, mas 1 year and 1 secondestá.

Componentes diferentes têm unidades de tempo diferentes. Portanto, não há unidades repetidas como em 5 seconds and 1
second.

Um componente não aparecerá se seu valor for zero. Portanto, 1 minute and 0 secondsnão é válido, mas deveria ser 1
minute.

Uma unidade de tempo deve ser usada "tanto quanto possível". Isso significa que a função não deve retornar 61 seconds,
mas 1 minute and 1 secondsim . Formalmente, a duração especificada por de um componente não deve ser maior do que
qualquer unidade de tempo válida mais significativa."""

def format_duration(seconds):
    if seconds <= 0:
        return "now"

    years = seconds // 31536000
    resto = seconds % 31536000
    days  = resto // 86400
    resto = resto % 86400
    hours = resto // 3600
    resto = resto % 3600
    minutes = resto // 60
    resto = resto % 60

    components = [
        (years, "year", "years"),
        (days, "day", "days"),
        (hours, "hour", "hours"),
        (minutes, "minute", "minutes"),
        (resto, "second", "seconds")
    ]

    res = []

    for value, singular, plural in components:
        if value > 0:
            if value == 1:
                res.append("1" + " " + singular)
            else:
                res.append(str(value) + " " + plural)
    return ", ".join(res[:-1]) + " and " + res[-1] if len(res) > 1 else res[0]

# Teste

print(format_duration(31536200))
print(format_duration(40))
