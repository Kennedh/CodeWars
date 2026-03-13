"""
In this Kata, you will be given a string and your task will be to return the length of the longest prefix that is also
a suffix. A prefix is the start of a string while the suffix is the end of a string. For instance, the prefixes of the
string "abcd" are ["a","ab","abc"]. The suffixes are ["bcd", "cd", "d"]. You should not overlap the prefix and suffix.

for example:
solve("abcd") = 0, because no prefix == suffix.
solve("abcda") = 1, because the longest prefix which == suffix is "a".
solve("abcdabc") = 3. Longest prefix which == suffix is "abc".
solve("aaaa") = 2. Longest prefix which == suffix is "aa". You should not overlap the prefix and suffix
solve("aa") = 1. You should not overlap the prefix and suffix.
solve("a") = 0. You should not overlap the prefix and suffix.
All strings will be lowercase and string lengths are 1 <= length <= 500

More examples in test cases. Good luck!


"""

def solve(st):
    max_length = 0
    n = len(st)
    for i in range(1, n // 2 + 1):
        prefix = st[:i]
        suffix = st[-i:]
        if prefix == suffix:
            max_length = i
    return max_length

# Teste

print(solve("abcd"))     # 0
print(solve("abcda"))    # 1
print(solve("abcdabc"))  # 3
print(solve("aaaa"))     # 2
print(solve("aa"))       # 1
print(solve("a"))        # 0