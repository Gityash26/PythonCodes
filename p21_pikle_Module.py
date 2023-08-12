'''
_________________________________________________________________________________________________
======================================Pickle Module==============================================
=================================================================================================
-> Pickle is like DATABASE that is used to store data at permanent basis instead of writing simply into text file
-> Pickle module is used to Serialize->(Write into file) and Decerilize->(Read from file) in python.

-> Following datatypes supports pickle(storing) : 
Bool , Int , Float , Complex , Strings , Tuples , Lists , Sets , Dictionary



_________________________________________________________________________________________________
======================================Pickle Methods==============================================
=================================================================================================

=> dump(obj,file) : Dumps object into the file
=> load(file) : Load object from the file

_________________________________________________________________________________________________
============================================Modes================================================
=================================================================================================
=> wb -> Write Binary
=> rb -> Read Binary
'''

import pickle

d={'Name':'Yash','Roll':'77','Course':'BCA'}

Myfile=open('abc.txt','wb')
pickle.dump(d,Myfile)
Myfile.close()



Myfile=open('abc.txt','rb')
l=pickle.load(Myfile)
print(l)

