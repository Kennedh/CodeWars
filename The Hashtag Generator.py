"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized, and remaining letters lowercased.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""

def generate_hashtag(s):
    if not s:
        return False
    res = [w.capitalize() for w in s.split()]
    res = "#" + "".join(res)
    return res if len(res) <= 140 else False

# Teste


print(generate_hashtag('Ola mundo python'))
print(generate_hashtag('    Olá     tudo   bem '))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('cOdEwArS is nIcE'))
print(generate_hashtag('python'))
print(generate_hashtag(''))