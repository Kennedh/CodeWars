"""
Tarefa Kata
Eu tenho um gato e um cachorro.

Ganhei-os na mesma época que o gatinho/cachorrinho. Isso foi humanYearshá anos.

Retornar suas respectivas idades agora como [ humanYears, catYears, dogYears]

NOTAS:

humanYears>= 1
humanYearssão apenas números inteiros
Anos de gato
15anos de gato para o primeiro ano
+9anos de gato para o segundo ano
+4anos de gato para cada ano depois disso
Anos de cão
15anos de cachorro para o primeiro ano
+9anos de cachorro para o segundo ano
+5anos de cachorro para cada ano depois disso
Referências

http://www.catster.com/cats-101/calculate-cat-age-in-cat-years
http://www.slate.com/articles/news_and_politics/explainer/2009/05/a_dogs_life.html
"""

def human_years_cat_years_dog_years(human):
    cat = 0
    dog = 0
    for n in range(human):
        if n == 0:
            cat += 15
            dog += 15
        if n == 1:
            cat += 9
            dog += 9
        if n > 1:
            cat += 4
            dog += 5
    return [human,cat,dog]

# Teste

print(human_years_cat_years_dog_years(1))
print(human_years_cat_years_dog_years(2))
print(human_years_cat_years_dog_years(5))
print(human_years_cat_years_dog_years(15))
print(human_years_cat_years_dog_years(20))
print(human_years_cat_years_dog_years(30))
