'''
_________________________________________________________________________________________________
=========================================Exception===============================================
=================================================================================================
Exceptions refers to some unexpected errors that cause program crashing.
Exceptions are cause due o some unexpected input or error that create a program crash without any notice or reason.





_________________________________________________________________________________________________
=====================================Types OF Exception==========================================
=================================================================================================

-> SyntaxError: 
This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

-> TypeError: 
This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.

-> NameError: 
This exception is raised when a variable or function name is not found in the current scope.

-> IndexError: 
This exception is raised when an index is out of range for a list, tuple, or other sequence types.

-> KeyError: 
This exception is raised when a key is not found in a dictionary.

->ValueError: 
This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.

-> AttributeError: 
This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.

->IOError: 
This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.

-> ZeroDivisionError: 
This exception is raised when an attempt is made to divide a number by zero.

-> ImportError: 
This exception is raised when an import statement fails to find or load a module.




_________________________________________________________________________________________________
==============================Syntax of Exception Handling=======================================
=================================================================================================

try:
    # code that may cause exception
except <exception>:
    # code to run when exception occurs




Note: Empty Except are used to handle any type of error means at th occurence of any type of exception That except always runs.

That's why we can handle specific error also by mention its type of exception after the except.
'''


def SimpleHandling():  
    print("\n\nSimple Except HAndling : ")
    try:
        num=int(input("\nEnter an Integer : "))          
        print(f"\nYour Num : {num}")

    except:
        print("Sorry But Only Integers Allowed")

SimpleHandling()





'''
_________________________________________________________________________________________________
==============================Specific Exception Handling=======================================
=================================================================================================
'''
# Note : finally block in exception handling always runs even when we use in function and control return from try block
# or after occurrence of any exception finally is always runs 

def Specif_Handling():

    print("\n\nSpecific Simple Except HAndling : ")

    try:
        a=int(input("\nEnter index (0 to 3) : "))
        print(f"\n=> Value error not occurred : {a}")
        b=[2,3,4,5]

        print(f"\n=> Index error not occurred : {b[a]}")
        return

    except ValueError:
        print("\n!! Index should be integer")

    except IndexError:
        print("\n!! Index must be under (0 to 3)")

    finally:
        print("\n~~~~~~~~~~~~~~~~~~~~Thankyou and GoodBye~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


Specif_Handling()




'''
_________________________________________________________________________________________________
==============================Custom Exception Handling=======================================
=================================================================================================
When their is no exception occurrence situation but still user implement their own limitation at run time 
Then we require to raise custom errors
ex : If a user says only integers allowed then it can be resolved using ValueError
     But now user says integer but from 1 to 10 only
     That time normal exception handling doesn't recognize this and we wants to raise our own exception condition

     ==> raise: keyword used to raise custom errors
'''


def customException():
    print("\n Custom Exception Handling : ")

    try:
        num=int(input("\nEnter a num between (1 to 10) : "))

        if num>=1 and num<=10:
            print(f"\nYour Choice : {num}")
        else:
            raise ValueError


    except ValueError:
        print("\n!! Number is not Int (OR) Out of the limit (1 to 10)")



customException()









