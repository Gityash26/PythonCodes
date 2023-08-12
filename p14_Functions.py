'''
_________________________________________________________________________________________________
====================================Functions in Python==========================================
=================================================================================================

Functions is a block of code that is createad to perform a specific type of task.
Functions helps to breakown the entire complex program int smaller modules and each module can be individually debug and test
functions are only execute when programmer creates a function call using its name

Functions are also helps to implement DRY(Do not repeat yourself) principle where,
If we require to perform same type of task for different value then instead of writing the same code multiple times just create a block of code and call for different value

-> Increase Readibility
-> Increase Reusability
-> Easy to debug and find errors
-> Reduce code size
-> Reduce Complexity


syntax : 
           def func_name():
               statement 1
               statement n
               
'''


def greet():
    print("\nHello Good Morning")

greet()




'''
_________________________________________________________________________________________________
====================================Functions with Argument======================================
=================================================================================================
-> Default Argument
   We can provide default value to arguments dclaration in function
   So that if we provide arguments during function call they are used and if not the default can be used automatically

-> Keyword Argument
   During function call we can cahnge the argument order by defining the keyword that we ae using for in function

-> Required Argument
   Those arguments or parameters that are definately required for making a function call

-> Variable Length Argument
   When we don't know about how much arguments we required to pass so variable length arguments helps to access those arguments ar run time
'''




# Default Argument________________________________________________________________________

print("\nImplementing Default Argument :") 

def Greet(name="Unknow"):
    print(f"\nHello {name}")

Greet()
Greet('Yash')

# ______________________________________________________________________________________________________



# Keyword Argument______________________________________________________________________________________

print("\nImplementing Keyword Argument :") 
def myself(name,age):
    print(f"\nMy name is {name} and I am {age} years old")

myself(age=21,name='Yash')

# ______________________________________________________________________________________________________







# Required Argument______________________________________________________________________________________

print("\nImplementing Required Argument :") 
def Required_myself(name,age=18):
    print(f"\nMy name is {name} and I am {age} years old")

Required_myself('Yash')

# ______________________________________________________________________________________________________







#--> Variable Lengh Argument______________________________________________________________________________________

# num is accepted as tuple 
def average(*num):
    sum=0
    for i in num:
        sum=sum+i
    print(f"Average of {num} : {sum/len(num)}")

average(2,3,4,5,6,7,78)







# num is accepted as Dictionary 
def name(**myname):
    print(f"Hello {myname['fname']} {myname['lname']}")

name(fname='Yash',lname='Sharma')


# ______________________________________________________________________________________________________









