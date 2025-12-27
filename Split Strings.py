"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number
of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    temp = ""
    res = []
    for l in s:
        temp += l
        if len(temp) == 2:
            res.append(temp)
            temp = ""
    if temp != "":
        res.append(temp + "_")
    return res

# Teste

print(solution("asdfadsf"))
print(solution("asdfads"))
