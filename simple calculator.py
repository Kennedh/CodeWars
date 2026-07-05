"""
You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or
division of two numbers.

Your function will accept three arguments:
The first and second argument should be numbers.
The third argument should represent a sign indicating the operation to perform on these two numbers.

You should return the result of applying the given operation to these numbers.

Note: In dynamically typed languages (JS, PHP, Python), the first and second arguments can be not numbers. In that
case, return "unknown value".

If the given operation to perform on the two numbers is not one of the four mentioned above, you should:

return a value:
"unknown value" (JS, PHP, Python)
throw an exception:
std::invalid_argument (C++)
ArgumentException (C#)
IllegalArgumentException (Java)
Example:
arguments: 1, 2, "+"
should return 3

arguments: 1, 2, "&"
refer to the description for what you should return in this case

# Specifically for dynamically-typed languages:

arguments: 1, "k", "*"
should return "unknown value"
"""

def calculator(x, y, op):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "unknown value"
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        if y == 0:
            return "unknown value"
        return x / y
    else:
        return "unknown value"

# Teste

print(calculator(6, 2, '+'))
print(calculator(4, 3, '-'))
print(calculator(5, 5, '*'))
print(calculator(5, 4, '/'))
print(calculator(6, 2, '&'))