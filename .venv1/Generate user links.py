"""
Sua tarefa é criar links de usuário para a URL. Você receberá um nome de usuário e deverá retornar um link válido.
"""
from setuptools.package_index import user_agent


def generate_link(user):
    encoding = {
        ' ': '%20',
        '!': '%21',
        '"': '%22',
        '#': '%23',
        '$': '%24',
        '%': '%25',
        '&': '%26',
        '\'': '%27',
        '(': '%28',
        ')': '%29',
        '*': '%2A',
        '+': '%2B',
        ',': '%2C',
        '/': '%2F',
        ':': '%3A',
        ';': '%3B',
        '<': '%3C',
        '=': '%3D',
        '>': '%3E',
        '?': '%3F',
        '@': '%40',
        '[': '%5B',
        '\\': '%5C',
        ']': '%5D',
        '^': '%5E',
        '`': '%60',
        '{': '%7B',
        '|': '%7C',
        '}': '%7D'
    }
    res = ""
    unreserved = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.~/')
    for char in user:
        if char in unreserved:
            res += char
        elif char in encoding:
            res += encoding[char]
        else:
            res += char
    return "http://www.codewars.com/users/" + res

# Teste

print(generate_link('matt c'))