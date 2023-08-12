
'''
_________________________________________________________________________________________________
====================================LIST in Python=============================================
=================================================================================================
-> List is a Mutable Datatype in python
-> Declared in 'square []' bracket with ' coma(,) ' sepated values.
-> List can store any type of values.
-> List slicing is also supported

'''

l=[2,40,92,"Apple",'Fruit',True]

print("\nPrinting List : ",l)

print("\nList Slicing : ",l[0:4])


print("\nList Iteration with Range()")
for i in range(0,len(l)):
    print(l[i])


print("\nList Iteration without Range()")
for i in l:
    print(i)



'''
_________________________________________________________________________________________________
====================================LIST Compprehension============================================
=================================================================================================
Also considered as short hand technique
'''

# _________________________________________________________________________________________________
mylist=[m for m in range(1,101)]
print("List Comprehension : \n",mylist)

# _________________________________________________________________________________________________

mylist=[m for m in range(1,101) if m%2==0]
print("\nList Comprehension for Even : \n",mylist)
# _________________________________________________________________________________________________

s="Hello World"
d=[value for value in s]
print("\nList Comprehension String : \n",d)
# _________________________________________________________________________________________________



'''
_________________________________________________________________________________________________
====================================Functions of LIST============================================
=================================================================================================
insert(index,value)	: Adds an element at the specified position
append(value)	: Adds an element at the end of the list
extend()    	: Add the elements of a list (or any iterable), to the end of the current list
clear()	        : Removes all the elements from the list
copy()	        : Returns a copy of the list
count(value)    : Returns the number of elements with the specified value
index(value)	    : Returns the index of the first element with the specified value
remove(value)	    : Removes the Specific Value
pop(index)	        : Delete the Specific Indexed Value and Return it
del(index)          : Delete the Specific Indexed Value
sort()	            : Sort the list
reverse()	        : Reverses the order of the list
max()               : Returns the Max value
min()               : Return the minimum Value
'''

print("\nMaximum Value : ",max(mylist))
print("\nMinimum Value : ",min(mylist))




'''
_________________________________________________________________________________________________
====================================zip() Functions============================================
=================================================================================================
It helps in the iteration of more than one list or tuple at the same time in equal amount.
'''

a="Hello Aple"
b="Hello Orange"

for i,j in zip(a,b):
    print(i , j)

