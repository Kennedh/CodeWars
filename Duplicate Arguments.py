"""
Complete the solution so that it returns true if it contains any duplicate argument values, and false otherwise.
Any number of arguments may be passed into the function.

The arguments passed in will only be strings or numbers.

Examples:

solution(1, 2, 3)             -->  false
solution(1, 2, 3, 2)          -->  true
solution('1', '2', '3', '2')  -->  true
"""

def solution(*args):
    return True if len(set(args)) != len(args) else False

# Teste

print(solution('a', 'b', 'c', 'c'))
print(solution('a', 'b', 'c', 'd'))