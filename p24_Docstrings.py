'''
====================================================================================================
=========================================Docstrings in Python=======================================
====================================================================================================

Docstrings seems similar like comments but they are totally dfferent concepts.

Strings in python are used to add short discriptions in program and also comments are totally ignored by the interpreter.

Docstring are used in functions, methods, class, or module to add documentation inside the code.

Docstrings can be access through docstring attribute.


====================================================================================================
=========================================Docstrings in Syntax=======================================
====================================================================================================
Whenever any tring literal is wriiten just over the function, module, or class defination it is considered as docstring and can be access through docstring atribute.
'''

def add(n1,n2):
    '''This function takes two integers and print their Sum'''
    print(f"\nSolution : {n1} + {n2} : {n1+n2}")


print(add.__doc__)         #Doc Attribute
add(10,20)
