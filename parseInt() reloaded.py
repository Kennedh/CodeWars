"""
Neste kata, queremos converter uma string em um inteiro.
As strings simplesmente representam os números em palavras.
"""

def parse_int(words):
    units = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19
    }
    tens = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }
    scales = {
        "hundred": 100, "thousand": 1000, "million": 1000000
    }

    current = 0
    total = 0
    words = words.replace("-", " ").replace(" and", " ")  # Normalize hyphens and 'and'
    for word in words.split():
        if word in units:
            current += units[word]
        elif word in tens:
            current += tens[word]
        elif word == "hundred":
            current *= scales[word]
        elif word in scales:
            total += current * scales[word]
            current = 0
    return total + current

# Teste

print(parse_int('two hundred forty-six'))