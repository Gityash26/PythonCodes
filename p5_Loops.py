
'''
_________________________________________________________________________________________________
=================================LOOPS In Python=============================================
=================================================================================================
Loops in python facilitate to perform any repeated task just by applying the concept of loops instead of writing it multiple times.
It also helps for the ittration of string, list, dictionary, sets, tuple, file etc) 

**Types of Loops : ****
(1) for loop
(2) While loop


-> Range(): Range function can be used with the loops and other methods. It helps to provide the values between the range 
   of any starting value to end value

syntax: range(Starting_Value, End_Value, Step difference)

'''

# for loop statement
print("\nFor loop with Range()")
for i in range(1,10):
    print(i*2)


# for loop itteration 
print("\nFor loop Iteration")
a=[2,4,6,8,20,30,40,50]
for i in a:
    print(i)


# for loop with else
print("\nFor loop with else")
a=(1,3,5,7,9)
for i in a:
    print("Value : ",i)
else:
    print("The End")


# While loop :
print("\nWhile loop")
a=10
while a>=5:
    print(a,end=" ")
    a=a-1

