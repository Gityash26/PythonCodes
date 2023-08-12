
'''
_________________________________________________________________________________________________
===============================Conditional Statement=============================================
=================================================================================================
(1) if Statement
(2) if else Statement
(3) elif Statement
(4) Match case Statement
'''




# If statement:
print("\n\nUsing If Statement")
age=19
if age>18:
    print("Eligible to Vote")



# If else Statement:
print("\n\nUsing If else Statement")

num=int(input("Enter a number : "))
if num%2==0:
    print(f"{num} is a Even number")
else:
    print(f"{num} is a Odd number")



# Elif Statement:
print("\n\nUsing Elif else Statement")

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")




# Match case : Match case is just similar to swith case in python
#              break is not required
print("\n\nUsing Match case Statement")

x=2
match x:
    case 0:
        print("Num is 0")
    
    case 1:
        print("Num is 1")

    case 2:
        print("Num is 2")
    
    case 3:
        print("Num is 3")
    
    case _ if x<1:
        print("x is negative")
    
    case _ if x!=5:
        print("x not 5")





# short hand technique for if else 
r=2
print("\nYash")if r == 1 else print("\nSanjay")if r == 2 else print("\nInvalid")