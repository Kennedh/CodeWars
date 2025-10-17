"""
Hopefully other examples can make this clearer.

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
mix(s1, s2) --> "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh"
Note for Swift, R, PowerShell
The prefix =: is replaced by E:

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
mix(s1, s2) --> "1:mmmmmm/E:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/E:ee/E:ss"
"""


def mix(s1, s2):
    result = []

    letters = set([c for c in s1 if c.islower()] + [c for c in s2 if c.islower()])

    for char in letters:
        count1 = s1.count(char)
        count2 = s2.count(char)

        if max(count1, count2) < 2:
            continue

        if count1 > count2:
            result.append(('1', char * count1))
        elif count2 > count1:
            result.append(('2', char * count2))
        else:
            result.append(('=', char * count1))

    result.sort(key=lambda x: (-len(x[1]), x[0], x[1]))

    return '/'.join(f"{prefix}:{chars}" for prefix, chars in result)





print(mix("Are they here", "yes, they are here"))