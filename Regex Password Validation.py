"""
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a digit
only contains alphanumeric characters (note that '_' is not alphanumeric)
"""

regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"

import re

def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$"

    if re.match(pattern, password):
        return True
    return False

# Testes

print(validate_password("abc123"))  # False (falta maiúscula)
print(validate_password("abcABC1"))  # True  (atende tudo)
print(validate_password("abABC1_"))  # False (contém caractere inválido '_')
print(validate_password("aB1"))  # False (muito curto)