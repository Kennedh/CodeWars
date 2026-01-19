"""In order to prove it's success and gain funding, the wilderness zoo needs to prove to environmentalists that it has
x number of mating pairs of bears.

Task:
You must check within a string (s) to find all of the mating pairs, returning a list/array of the string containing
valid mating pairs and a boolean indicating whether the total number of bears is greater than or equal to x.

Rules for a 'valid' mating pair:
Bears are either 'B' (male) or '8' (female),
Bears must be together in male/female pairs 'B8' or '8B',
Mating pairs must involve two distinct bears each ('B8B' may look fun, but does not count as two pairs).
Return an array containing a string of the valid mating pairs available (empty string if there are no pairs), and a
boolean indicating whether the total number of bears is greater than or equal to x. , e.g:

(6, 'EvHB8KN8ik8BiyxfeyKBmiCMj') ---> ['B88B', false]; in this example, the number of bears(=4) is lesser than the
given value of x(=6)"""


def bears(x, s):
    pairs = []
    i = 0
    n = len(s)

    while i < n - 1:
        if (s[i] == 'B' and s[i + 1] == '8') or (s[i] == '8' and s[i + 1] == 'B'):
            pairs.append(s[i] + s[i + 1])
            i += 2
        else:
            i += 1
    pairs_string = ''.join(pairs)
    total_bears = len(pairs) * 2
    is_greater_or_equal = total_bears >= x

    return [pairs_string, is_greater_or_equal]

# Teste

print(bears(6, 'EvHB8KN8ik8BiyxfeyKBmiCMj'))