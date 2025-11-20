"""
Your goal is to return multiplication table for number that is always an integer from 1 to 10.

For example, a multiplication table (string) for number == 5 looks like below:

1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
P. S. You can use \n in string to jump to the next line.

Note: newlines should be added between rows, but there should be no trailing newline at the end. If you're unsure about
the format, look at the sample tests.
"""

def multi_table(number):
    return (f"1 * {number} = {number * 1}\n"
            f"2 * {number} = {number * 2}\n"
            f"3 * {number} = {number * 3}\n"
            f"4 * {number} = {number * 4}\n"
            f"5 * {number} = {number * 5}\n"
            f"6 * {number} = {number * 6}\n"
            f"7 * {number} = {number * 7}\n"
            f"8 * {number} = {number * 8}\n"
            f"9 * {number} = {number * 9}\n"
            f"10 * {number} = {number * 10}")

# Teste

print(multi_table(5))