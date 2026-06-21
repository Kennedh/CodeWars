"""
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Calculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
"""

def twice_as_old(dad_years_old, son_years_old):
    target = son_years_old * 2
    res = dad_years_old - target
    return res if res > 0 else res * -1

# Teste

print(twice_as_old(36,7))
print(twice_as_old(55,30))
print(twice_as_old(42,21))
print(twice_as_old(22,1))
print(twice_as_old(29,0))