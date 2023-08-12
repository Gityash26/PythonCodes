'''
_________________________________________________________________________________________________
====================================Tuples in Pyhon==============================================
=================================================================================================

=> Tuple in python is s immutable datatype.
=> Tuple store value at Indexed manner
=> Tuple supports Tuple Slicing
=> Represented in () -> circular brackets
=> Tuples elements are never be changed or manipulates

syntax: 

t=()    Empty tuple
t=(1,)  Tuple with one element
t=(1)   This is a wrong way to create tuple with one element
'''


T=(1,2,5,2,4.6,True,'Yash')
print(T)


'''
_________________________________________________________________________________________________
==================================Methods of Tuples==============================================
=================================================================================================

count() : returns count of the element in the tuple

index() : returns the index of the element in the tuple
'''

print("\n",T[0:3])

print(f"\nThe num 2 arrives in Tuple :  {T.count(2)} Times")

print(f"\nThe value 'Yash' arrives in Tuple at Index :  {T.index('Yash')}")

