"""
O gerente de marketing da sua startup informou que seu site tem um grande público na Escandinávia e nos países vizinhos.
O departamento de marketing acha que seria ótimo receber os visitantes do site no idioma deles. Felizmente, você já usa
uma API que detecta a localização do usuário, então essa é uma vitória fácil.

A Tarefa
Pense em uma maneira de armazenar os idiomas como um banco de dados. Os idiomas estão listados abaixo para você copiar
e colar!
Escreva uma função de "boas-vindas" que receba o parâmetro "idioma", do tipo String, e retorne uma saudação — se você a
tiver no seu banco de dados. O padrão deve ser o inglês se o idioma não estiver no banco de dados ou em caso de uma
entrada inválida.
O Banco de Dados
Modifique isso conforme apropriado para seu idioma.

[ ("english", "Welcome")
, ("czech", "Vitejte")
, ("danish", "Velkomst")
, ("dutch", "Welkom")
, ("estonian", "Tere tulemast")
, ("finnish", "Tervetuloa")
, ("flemish", "Welgekomen")
, ("french", "Bienvenue")
, ("german", "Willkommen")
, ("irish", "Failte")
, ("italian", "Benvenuto")
, ("latvian", "Gaidits")
, ("lithuanian", "Laukiamas")
, ("polish", "Witamy")
, ("spanish", "Bienvenido")
, ("swedish", "Valkommen")
, ("welsh", "Croeso")
]
Possíveis entradas inválidas incluem:

IP_ADDRESS_INVALID - not a valid ipv4 or ipv6 ip address
IP_ADDRESS_NOT_FOUND - ip address not in the database
IP_ADDRESS_REQUIRED - no ip address was supplied
"""


def greet(language):
    if language == "czech":
        return "Vitejte"
    elif language == "danish":
        return "Velkomst"
    elif language == "dutch":
        return "Welkom"
    elif language == "estonian":
        return "Tere tulemast"
    elif language == "finnish":
        return "Tervetuloa"
    elif language == "flemish":
        return "Welgekomen"
    elif language == "french":
        return "Bienvenue"
    elif language == "german":
        return "Willkommen"
    elif language == "irish":
        return "Failte"
    elif language == "italian":
        return "Benvenuto"
    elif language == "latvian":
        return "Gaidits"
    elif language == "lithuanian":
        return "Laukiamas"
    elif language == "polish":
        return "Witamy"
    elif language == "spanish":
        return "Bienvenido"
    elif language == "swedish":
        return "Valkommen"
    elif language == "welsh":
        return "Croeso"
    else:
        return "Welcome"

# teste

print(greet('english'))
print(greet('IP_ADDRESS_INVALID'))
print(greet('dutch'))