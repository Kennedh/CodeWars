"""
Complete o metodo/função para converter palavras delimitadas por hífen/sublinhado para Camel Case . A primeira palavra
na saída deve ser escrita em maiúscula somente se a palavra original já estiver em maiúscula (conhecido como Upper
Camel Case, também frequentemente chamado de Pascal Case). As próximas palavras devem ser sempre escritas em maiúscula.

Exemplos
"the-stealth-warrior"é convertido para"theStealthWarrior"

"The_Stealth_Warrior"é convertido para"TheStealthWarrior"

"The_Stealth-Warrior"é convertido para"TheStealthWarrior"


"""

def to_camel_case(text):
    if text == "":
        return ""
    up = 0
    res = ""
    for l in text:
        if not l.isalpha():
            up = 1
        elif up == 1:
            res += l.upper()
            up = 0
        elif isinstance(l, str):
            res += l
    return res

# Teste

print(to_camel_case("the_stealth_warrior"))