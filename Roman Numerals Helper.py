"""
Escreva duas funções que convertam um algarismo romano de e para um valor inteiro.
Vários valores de algarismos romanos serão testados para cada função.

Os algarismos romanos modernos são escritos expressando cada dígito separadamente,
começando pelo dígito mais à esquerda e pulando qualquer dígito com valor zero.
"""

class RomanNumerals:
    @staticmethod
    def to_roman(number):
        int_to_roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        result = ""
        for value, symbol in int_to_roman_map:
            while number >= value:
                result += symbol
                number -= value
        return result

    @staticmethod
    def from_roman(roman):
        roman_to_int_map = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        total = 0
        prev = 0
        for char in reversed(roman):
            curr = roman_to_int_map[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
                prev = curr
        return total

# Teste

print(RomanNumerals.to_roman(1525))