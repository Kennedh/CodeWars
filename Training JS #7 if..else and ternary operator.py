"""
In JavaScript, if..else is the most basic conditional statement, it consists of three parts:condition, statement1,
statement2, like this:

if condition: statementa
else:         statementb
It means that if the condition is true, then execute the statementa, otherwise execute the statementb. If the
statementa or statementb are more than one line, you need to add { and } at the head and tail of statements in JS,
to keep the same indentation on Python and to put an end in Ruby where it indeed ends.

For example, if we want to judge whether a number is odd or even, we can write code like this:

def odd_even(n):
    if n % 2: return "odd number"
    else:     return "even number"
If there is more than one condition to judge, we can use the compound if...else statement. For example:

def old_young(age):
    if age < 16:        return "children"
    elif age < 50:      return "young man" #use "else if" if needed
    else:               return "old man"
This function returns a different value depending on the parameter age.

Looks very complicated? Well, JS and Ruby also support the ternary operator and Python has something similar too:

statementa if condition else statementb
Condition and statement separated by "?", different statement separated by ":" in both Ruby and JS; in Python you put
the condition in the middle of two alternatives. The two examples above can be simplified with ternary operator:

def odd_even(n):
    return "odd number" if n % 2 else "even number"
def old_young(age):
    return "children" if age < 16 else "young man" if age < 50 else "old man"
Task:
Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:n, n is the number of hotdogs a
customer will buy, different numbers have different prices (refer to the following table), return how much money will
the customer spend to buy that number of hotdogs.
"""


def sale_hotdogs(n):
    if n < 5:
        preco = 100
    elif n < 10:
        preco = 95
    else:
        preco = 90
    return n * preco

# Teste

print(sale_hotdogs(0))
print(sale_hotdogs(1))
print(sale_hotdogs(2))
print(sale_hotdogs(3))
