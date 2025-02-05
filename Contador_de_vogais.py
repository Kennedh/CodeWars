def get_count(w):
    vowels = "aeiou"
    return sum(1 for l in w if l in vowels)

#Example

print(get_count("word"))
