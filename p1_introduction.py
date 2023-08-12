'''
_______________________________________________________________________________________
=============================================PYTHON====================================
=======================================================================================
Python is an Interpreted, Object Oriented, High level, Programming Language with Dynamic Semantics.

-> Interpreted : Read and execute line by line and stop when any error occured
              ex: python

-> compiler : Compile Entire code then execute the program 
              ex: C, C++, JAVA

-> Object oriented : Support structural, functional as well as class and object concepts 

-> High Level : Python is much User friendly and more english like sentences

-> Dynamic Semantic : Python Supports Automatic datatype detection feature

_________________________________________________________________________________________
========================================FEATURES OF PYTHON===============================
=========================================================================================
(1) Easy to Learn and Implement
(2) Open Source
(3) Broad Standard Library
(4) Portable with every OS
(5) High Level Language
(6) GUI programming supports
(7) Less Development Time

__________________________________________________________________________________________
==========================================APPLICATIONS OF PYTHON==========================
==========================================================================================
-> Network Programming
-> Data Analysis
-> Robotics
-> Web Applications (Jango)
-> Desktop Applications (Tinker library)
-> Game Development
-> Web Scraping
-> Data Visulalization
-> Scientific Calculation
-> Machine Learning
-> 3-D Application Development
-> Audio Videos Software Development

'''
'''
___________________________________________________________________________________________
=====================================FIRST PYTHON PROGRAM==================================
===========================================================================================
'''
print('Hello World (\')')
print("Hello World (\")")
print('''Hello World (\''')''')


'''
______________________________________________________________________________________
==========================================VARIABLES IN PYTHON=========================
======================================================================================
A Variable is a container of memeory that is used to store some values. VAriable is considerd to be some name given to a specific size of memory.
-> In python the memory is allocated to the value instead of variable
   ex: a=10 , b=10
   In this case both the variables access the same memory address that contains the value : 10

-> In C, C++ the memory is allocated to variable name

'''

a=10
b="Good Morning"
print("\nVARIABLES IN PYTHON : ")
print("a : ",a)
print("b : ",b)
print("Address of a: ",id(a))
print("Address of b: ",id(b))



'''
_______________________________________________________________________________________
======================================DATATYPE IN PYTHON================================
========================================================================================
DataType in python refers to the Type of value or data a variable stores.


                            ****DataTypes in python****
                __________________________|___________________________
               |                                                      |  
         MUTABLE DATATYPE                                      IMMUTABLE Datatype
               |                                                      |
            List                                               int, float, complex         
            Dictionary                                         String
            Byte array                                         Tuple, Sets


(1) Numeric: int, 
             float, 
             complex

(2) Sequence: string=""
              List=[]
              Tuple=()

(3) Dictionary={'key':'value'}

(4) Set={2,3,4}

(5) Bool= True,False

'''
print("\nDataTypes in python\n")
# Numeric datatype
a1=10
a2=2.8
a3=1+3j
print(f"a1 : {a1} \nDatatype : {type(a1)}")
print(f"a2 : {a2} \nDatatype : {type(a2)}")
print(f"a3 : {a3} \nDatatype : {type(a3)}")

# Sequence Datatype
b1="Good Morning"
b2=[10, 20, 30, "hello"]
b3=('yash',76,22.3)

print(f"\nb1 : {b1}     => Datatype : {type(b1)}")
print(f"\nb2 : {b2}     => Datatype : {type(b2)}")
print(f"\nb3 : {b3}     => Datatype : {type(b3)}")


# Dictionary Datatype
c1={'Name':"myname",
   'Fruit':'Apple'}

# Sets Datatype
d1={1,2,3,4,True,"yash"}

# Bool Datatype
e1=True
