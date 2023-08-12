
'''
_________________________________________________________________________________________________
=================================STRINGS In Python=============================================
=================================================================================================
String is a Datatype in python that refered to be as sequence of character within 
(Single quotes)  
(Double quotes) 
(Triple quotes)

'''
s1 = 'Hello python'
s2 = "Hello python"
s3 = '''Hello python'''


'''
_________________________________________________________________________________________________
=================================Indexing In String=============================================
=================================================================================================

s = " HELLO PYTHON"

Forard indexing   (---->) :           => 1 2 3 --------------- len(s)
Backward indexing (<----) :           => -len(s)-------------- -3 -2 -1




_________________________________________________________________________________________________
=================================Slicing In String=============================================
=================================================================================================
String slicing feature helps to print a part ofstring or upto and index just by using index values.
syntax:
         str_var [Start : End : Skip d/f]
'''
s1 = "Good morning"


print("\nString Slicing [start : End : Skip]")
print(s1[0: 4])
print(s1[:])
print(s1[0: -6])


print("\nString Iteration with range()")
for i in range(len(s1)):
    print(s1[i], end="")

print("\n\nString Iteration without range()")
for i in s1:
    print(i, end="")


'''
_________________________________________________________________________________________________
====================================String Functions=============================================
=================================================================================================
capitalize()	: Converts the first character to upper case
casefold()	    : Converts string into lower case
center()	    : Returns a centered string
count()	        : Returns the number of times a specified value occurs in a string
upper()	        : Converts a string into upper case
swapcase()	    : Swaps cases, lower case becomes upper case and vice versa
format()	    : Formats specified values in a string
find()	        : Searches the string for a specified value and returns the position of where it was found
index()	        : Searches the string for a specified value and returns the position of where it was found
endswith()	    : Returns true if the string ends with the specified value
lower()	        : Converts a string into lower case
replace()	    : Returns a string where a specified value is replaced with a specified value
join()	        : Converts the elements of an iterable into a string
split()	        : Splits the string at the specified separator, and returns a list
strip()	        : Returns a trimmed version of the string
splitlines()	: Splits the string at line breaks and returns a list
startswith()	: Returns true if the string starts with the specified value
title()	        : Converts the first character of each word to upper case
isalnum()	    : Returns True if all characters in the string are alphanumeric
isalpha()	    : Returns True if all characters in the string are in the alphabet
isascii()	    : Returns True if all characters in the string are ascii characters
isdecimal()	    : Returns True if all characters in the string are decimals
isdigit()	    : Returns True if all characters in the string are digits
isidentifier()  : Returns True if the string is an identifier
islower()	    : Returns True if all characters in the string are lower case
isnumeric()	    : Returns True if all characters in the string are numeric
isprintable()	: Returns True if all characters in the string are printable
istitle()	    : Returns True if the string follows the rules of a title
isupper()	    : Returns True if all characters in the string are upper case

chr()           : Returns character value of an ASCII value 

ord()           : Returns the ASCII value 
'''

Asci_value=ord('A')
chr_value=chr(Asci_value)

print(f"\n\nASCII (A) : {Asci_value}")
print(f"\nChar ({Asci_value}) : {chr_value}")



