"""
Desta vez, sem história, sem teoria. Os exemplos abaixo mostram como escrever uma função accum:

accum("abcd") -> "A-Bb-Ccc-Dddd"
"""

def accum(st):
    ad = 0
    t = ""
    res = ""
    for l in range(0,len(st)):
        ad += 1
        t = st[l] * ad
        if len(t) == 1:
            res += t
        else:
            res += f"-{t}".title()
    return res

# Teste

print(accum("abcd"))
print(accum("NyffsGeyylB"))
print(accum("ZpglnRxqenU"))





