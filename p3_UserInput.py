
'''
_________________________________________________________________________________________________
=================================Input() In Python=============================================
=================================================================================================
Input() function in python used to take input from the User at run time.
It always take input in the form of string so for the further use or operation we have to typecast Accordingly.
 
'''
n1=input("Enter first num : ")
n2=input("Enter Second num : ")
n1=int(n1)
n2=int(n2)
print(f"Sum : {n1+n2}")



# eval() can typecast int and float both
a=eval(input("Enter first Value : "))
b=eval(input("Enter Second Value : "))
print(f"a : {type(a)}")
print(f"b : {type(b)}")



