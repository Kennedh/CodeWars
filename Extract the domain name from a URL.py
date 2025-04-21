"""
Escreva uma função que, ao receber uma URL como string, analise apenas o nome do domínio e o retorne como uma string.
"""

def domain_name(url):
    url = url.replace("http://", "").replace("https://", "").replace("www.","")
    return  url.split(".")[0]

# Teste


print(domain_name("http://www.codewars.com/kata/"))