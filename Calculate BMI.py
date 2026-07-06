"""
Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
"""

def bmi(weight, height):
    b = weight / height ** 2
    return ["Underweight", "Normal", "Overweight", "Obese"][(b > 18.5) + (b > 25) + (b > 30)]

# Teste

print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(100, 1.80))