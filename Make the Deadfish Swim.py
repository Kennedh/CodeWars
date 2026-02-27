"""
Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.

Examples
Program "iiisdoso" should return numbers [8, 64].
Program "iiisdosodddddiso" should return numbers [8, 64, 3600].
"""

def parse(data):
    res = []
    num = 0
    for a in data:
        match a:
            case "i":
                num += 1
            case "d":
                num -= 1
            case "s":
                num = num ** 2
            case "o":
                res.append(num)
    return res

# Teste

print(parse("ooo"))
print(parse("ioioio"))
print(parse("idoiido"))
print(parse("isoisoiso")) # [1,4,25]
print(parse("codewars"))


