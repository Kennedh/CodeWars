"""
Description:
Remove all exclamation marks from the end of sentence.

Examples
"Hi!"     ---> "Hi"
"Hi!!!"   ---> "Hi"
"!Hi"     ---> "!Hi"
"!Hi!"    ---> "!Hi"
"Hi! Hi!" ---> "Hi! Hi"
"Hi"      ---> "Hi"
"""

def remove(st):
    res = list(st)
    while res[-1] == "!":
        res.pop()
    return "".join(res)

# Teste

print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("Hi! Hi!"))
print(remove("Hi"))


