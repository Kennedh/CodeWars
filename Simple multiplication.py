"""
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""

def simple_multiplication(number) :
    return number * 8 if number % 2 == 0 else number * 9

# Teste

print(simple_multiplication(2))
print(simple_multiplication(1))
print(simple_multiplication(8))
print(simple_multiplication(4))
print(simple_multiplication(5))
