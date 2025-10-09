"""
You need to create a function that converts the input into this format, with the output being the same string expect there is a pattern of uppercase and lowercase letters.

Example:

input:  "stop Making spongebob Memes!"
output: "StOp mAkInG SpOnGeBoB MeMeS!"
"""

def sponge_meme( s ):
    res = ""
    for idx, l in enumerate(s):
        if idx % 2 == 0:
            res += l.upper()
        else:
            res += l.lower()
    return res

# Teste

print(sponge_meme("The function didn't return anything. Did you print the result instead?"))