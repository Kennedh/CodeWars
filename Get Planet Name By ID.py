"""
The function is not returning the correct values. Can you figure out why?

Example (Input --> Output ):

3 --> "Earth"
"""

def get_planet_name(id):
    match id:
        case 1: return "Mercury"
        case 2: return "Venus"
        case 3: return "Earth"
        case 4: return "Mars"
        case 5: return "Jupiter"
        case 6: return "Saturn"
        case 7: return "Uranus"
        case 8: return "Neptune"

# Teste

print(get_planet_name(2))
print(get_planet_name(5))
print(get_planet_name(3))
print(get_planet_name(4))
print(get_planet_name(8))
print(get_planet_name(1))
