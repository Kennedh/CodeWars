"""
Você provavelmente conhece o sistema de "curtidas" do Facebook e de outras páginas.
As pessoas podem "curtir" posts de blogs, fotos ou outros itens.
Queremos criar o texto que deve ser exibido ao lado de cada item.
"""

def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    elif len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

# teste

print(likes([])) # 'no one likes this'
print(likes(['Peter'])) # 'Peter likes this'
print(likes(['Jacob', 'Alex'])) # 'Jacob and Alex like this'
print(likes(['Max', 'John', 'Mark'])) # 'Max, John and Mark like this'
print(likes(['Alex', 'Jacob', 'Mark', 'Max'])) # 'Alex, Jacob and 2 others like this'
