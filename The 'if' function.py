"""
Create a function that takes three arguments:

a value to be evaluated for truthiness.
a function to execute if the first argument is truthy.
a function to execute if the first argument is falsy.
If the first argument evaluates to truthy, call the second argument (a function). If it evaluates to falsy, call the
third argument instead (also a function).

In statically-typed languages, the first argument will be a boolean. In dynamically-typed languages that attribute a
truth value to all expressions, it may be of any type.
"""

def _if(value, truthy_fn, falsy_fn):
    if value:
        return truthy_fn()
    else:
        return falsy_fn()

# Teste

_if(True,
    lambda: print("It's true!"),
    lambda: print("It's false!")
)

_if("",
    lambda: print("Truthy value"),
    lambda: print("Falsy value")
)
