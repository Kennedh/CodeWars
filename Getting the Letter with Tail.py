"""
Letter with Tail
We got a string of letters made up by Os and/or Xs (or an empty string).

In this Kata, a Letter with Tail can be either one of the following:

O followed by 1 or more X, such as OX, OXX, OXXX, etc.

X followed by 1 or more O, such as XO, XOO, XOOO, etc.

Total Possible Amount
In most of the cases, we can find more than 1 way to get Letter with Tails.

And we are looking for the cases: Every single character from the input cannot occur in two or more different Letter
with Tails.

For example, input string is 'OXXO'

(We use parentheses to show the Letter with Tails we got in the example)

(OX)XO, (OXX)O, OX(XO), (OX)(XO)
There are 4 of them. We call the number total possible amount.

Task
Input: Getting a string of letters made up by Os and/or Xs (or an empty string).

Return: Return the total possible amount for the input string.

0 <= string length <= 90

With the string length limit, the answer will not be bigger than 2^64.

Example:
Input String is 'XOOOXXO'

1 Letter with Tail:

(XO)OOXXO, (XOO)OXXO, (XOOO)XXO, XOO(OX)XO, XOO(OXX)O, XOOOX(XO)


2 Letter with Tails:

(XO)O(OX)XO, (XO)O(OXX)O, (XO)OOX(XO), (XOO)(OX)XO, (XOO)(OXX)O, (XOO)OX(XO), (XOOO)X(XO), XOO(OX)(XO)


3 Letter with Tails:

(XO)O(OX)(XO), (XOO)(OX)(XO)
So the answer is 16.

Sample Tests:
Input => Output

'' => 0
'OOO' => 0
'XX' => 0
'XXXXO' => 1
'OXX' => 2
'OXOX' => 4
'OXXO' => 4
'XOXOX' => 7
'XOOOXXO' => 16
'XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO' => 63245985
"""


def total_possible_amount(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [0] * (n + 1)
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        dp[i] = dp[i + 1]
        char = s[i]
        target = 'X' if char == 'O' else 'O'
        j = i + 1
        while j < n and s[j] == target:
            dp[i] += dp[j + 1]
            j += 1
    return dp[0] - 1

# Teste

print(total_possible_amount(''))
print(total_possible_amount('OOO'))
print(total_possible_amount('XX'))
print(total_possible_amount('XXXXO'))
print(total_possible_amount('OXX'))
print(total_possible_amount('OXOX'))
print(total_possible_amount('OXXO'))
print(total_possible_amount('XOXOX'))
print(total_possible_amount('XOOOXXO'))
print(total_possible_amount('XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO'))