"""
Crie uma função que responda à pergunta "Você está tocando banjo?".
Se seu nome começa com a letra "R" ou "r" minúsculo, você está tocando banjo!
"""

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"

# Teste

print(are_you_playing_banjo("Ronaldo"))