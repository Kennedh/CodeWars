"""
Create a function named combineNames/combine_names/CombineNames that accepts two parameters (first and last name).
The function should return the full name.

Example:

With "James" as the first name and "Stevens" as the last name should return "James Stevens"
"""

def combine_names(str1, str2):
    return str1 + " " + str2

# Teste

print(combine_names("James", "Stevens"))
print(combine_names("Davy", "Back"))
print(combine_names("Arthur", "Dent"))
