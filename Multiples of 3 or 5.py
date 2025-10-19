"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If a number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)


"""

def solution(number):
    return sum([u for u in range(number) if u % 3 == 0 or u % 5 == 0])


# Teste

print(solution(9))