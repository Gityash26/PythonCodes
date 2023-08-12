'''
_________________________________________________________________________________________________
================================= TYPECASTING=============================================
=================================================================================================
Typecasting is a way to convert a datatype from one to another (only if possible)
'''
a=10
print(f"Value a : {a}  of Type : {type(a)}")
a=str(a)
print(f"Value a : {a}  of Type : {type(a)}")



'''
_________________________________________________________________________________________________
=================================Operators In Python=============================================
=================================================================================================
(1)-> Arithmetic Operator  :  [+ , - , * , / , ** , // etc]
(2)-> Assignment operator  :  [= , += , -= , *= , etc]
(3)-> Comparision Operator :  [== , <= , >= , != etc]
(4)-> Logical operator     :  [and , or , not] 
'''
x=8
y=2
print("\nArithmetic Operator ::") 
print(f"(x+y) : {x+y}")                                    
print(f"(x-y) : {x-y}")
print(f"(x*y) : {x*y}")
print(f"(x/y) : {x/y}")
print(f"(x**y): {x**y}")
print(f"(x//y): {x//y}")


print("\nAssignment Operator ::") 
x=10
print(f"(x=10)  : {x}")
x+=5
print(f"(x+=10) : {x}")
x-=2
print(f"(x-=10) : {x}")
x*=2
print(f"(x*=10) : {x}")
x/=2
print(f"(x/=10) : {x}")


print("\nComparision Operator ::") 
x=10
b=30
print(f"(x==y) : {x==y}")
print(f"(x<=y) : {x<=y}")
print(f"(x>=y) : {x>=y}")
print(f"(x!=y) : {x!=y}")

print("\nLogical Operator ::")
age=25 
marks=89

if age>18 and marks>75:
    print("Logical AND operator : Both are True") 

if age>18 or marks<75:
    print("Logical OR operator  : Any one is True") 

if not age<18:
    print("Logical NOT operator : True -> False") 



'''
_________________________________________________________________________________________________
=================================MEMBERSHIP OPERATOR=============================================
=================================================================================================
Membership operator 'in' or 'not in' can be used to find the existence of any value or we can say that a value is a member of any list, dictionary, tuple,set, etc without using any loops.
These operators are most used operators in python.
(1)-> in operator
(2)-> not in operator
'''
a=[2,4,9,10,22,34]

if 4 in a:
    print("\n-> Using 'in' operator : True 4 is present")

if 1 not in a:
    print("\n-> Using 'not in' operator : True 1 is not present")
    



'''
_________________________________________________________________________________________________
===================================IDENTITY OPERATOR=============================================
=================================================================================================
Identity Operator 'is' or 'is not' in python are act a '==' or '!=' Operators.
But their is one difference between 'is' and '==' operator
-> '==' operator used to check if two values are equal or not.
    ex: a==b:
        value(a) == value(b)

-> 'is' operator used two check if the memory reference of both the values are same or not.
    ex: a is b:
    id(a) == id(b)
    
'''
a=[1,2,3]
b=a
c=a[:]
print(a==b)
print(a==c)
print(a is b)
print(a is not c)




'''
_________________________________________________________________________________________________
====================================BITWISE OPERATOR=============================================
=================================================================================================
Bitwise operator operates on bit values (0 and 1)
-> '&' And operator  (x & y)
-> '|' OR perator    (x | y)
-> '^' XOR operator  (x ^ y)

bin() : In built bin function helps to provide the binary value of a number

______________________________________________________________
|____A____|____B____||___A & B____|____A | B____|____A ^ B____|
|    0    |    0    ||     0      |      0      |      0      |
|    0    |    1    ||     0      |      1      |      1      |
|    1    |    0    ||     0      |      1      |      1      |
|    1    |    1    ||     1      |      1      |      0      |
|_________|_________||____________|_____________|_____________|

'''
print("\nBitwise operation : ")
a=10
b=8
print(f"\n(a & b) => ({a} & {b}) => ({a&b}) \n-> ({bin(a)} & {bin(b)}) => ({bin(a&b)})")
print(f"\n(a | b) => ({a} | {b}) => ({a|b}) \n-> ({bin(a)} | {bin(b)}) => ({bin(a|b)})")
print(f"\n(a ^ b) => ({a} ^ {b}) => ({a|b}) \n-> ({bin(a)} ^ {bin(b)}) => ({bin(a^b)})")

