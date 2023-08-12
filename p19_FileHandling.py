
'''
_________________________________________________________________________________________________
====================================Files in python==============================================
=================================================================================================
As w know Ram is a versatile memeory that erase all the data generated during a process after its termination.
So that if we wants to store those data or retreive and stored data then we required the concept of files.




_________________________________________________________________________________________________
====================================Types of Files in Python=====================================
=================================================================================================
File are of two types : 

(1)-> Text Files
      --> .txt

(2)-> Binary Files
      --> .bin

      
_________________________________________________________________________________________________
==============================Advantages od File Handling========================================
=================================================================================================

Versatility: 
Provide various methods or operations like creating, Deleting, Appending, Reading, Writing a file

Flexibility: 
File handling allows to work with different file types (text files, binary files, CSV files, etc.)
And perform different operations on files (read, write, append, etc)

User–friendly: 
Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.

Cross-platform: 
Python file-handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.


_________________________________________________________________________________________________
==============================Disadvantages od File Handling=====================================
=================================================================================================

Error-prone: 
File handling operations in Python can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).

Security risks: 
File handling in Python can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.

Complexity: 
File handling in Python can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.

Performance: 
File handling operations in Python can be slower than other programming languages, especially when dealing with large files or performing complex operations.








_________________________________________________________________________________________________
===================================== File Handling Methods======================================
=================================================================================================

(1) open("filename" , "mode") : It helps to open a file in a specific mode of opening-> (Read, Write, Append)

(2) with open("filename", "mode") as f:

(3)write(content) : Write into file

(4)read() : Read entire content from file

(5)readline() : Read line by line content from file


=================================================================================================
===> Opening Modes In Python
=================================================================================================

r: open an existing file for a read operation.

w: open an existing file for a write operation. 
   If the file already contains some data then it will be overridden but 
   if the file is not present then it creates the file as well.

a:  open an existing file for append operation.
    It would not override existing data.

r+:  To read and write data into the file. 
     The previous data in the file will be overridden.

w+: To write and read data. 
    It will override existing data.

a+: To append and read data from the file. 
    It would not override existing data.
'''


def write():
    try:
        with open("abc.txt","w")as f:
            text=input("Enter Your content : ")
            f.write(text)
    except:
        print("Unknown Error Occured")
          
def read():
    try:
        with open("abc.txt","r")as f:
            text=f.read()
            print(f"\nFile Content : {text}")
    except:
        print("Unknown Error Occured")
      
def append():
    try:
        with open("abc.txt","a")as f:
            text=input("Enter Appended content : ")
            f.write(text)
    except:
        print("Unknown Error Occured")



while True:
    ch=input("\nEnter Operation : \n(1)Write\n(2)Read\n(3)Append\n====> ")
    if ch=='1':
        write()
    elif ch=='2':
        read()
    elif ch=='3':
        append()
    else:
        break
    