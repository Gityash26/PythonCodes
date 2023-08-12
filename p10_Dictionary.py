'''
_________________________________________________________________________________________________
================================Dictionary in Python=============================================
=================================================================================================
Dictionary is an Unordered Datatype in python
Dictionary consist of key : value pairs in {} -> curly braces
=> key of dictionary should be unique
=> values can be multiples

syntax : dict_name={'key1' : 'pair1',
                    'key2' : 'pair2',
                    'key3' : 'pair3'
                    }

    
Properties of Dictionary : 
=> Mutable
=> Unordered
=> Unindexed
=> Unique Keys

Note : Data from the DataBase are retreive in the form of key : Value Pairs
'''

d = {'R1': 'Yash',
     'R2': 'Sanjay',
     'R3': 'Kunal',
     'R4': 'Sachin'}


print(d['R1'])
print(d.get('R2'))

# Throw error if key ws not found
# print(d['R9'])


# Throw None if ke was not found
print(d.get('R9'))


'''
_________________________________________________________________________________________________
=================================Dictionary Methods==============================================
=================================================================================================

clear()          : Clear all dictionary
copy()	       : Returns a copy of the dictionary
fromkeys()	  : Returns a dictionary with the specified keys and value
get()	       : Returns the value of the specified key
items()	       : Returns a list containing a tuple for each key value pair
keys()	       : Returns a list containing the dictionary's keys
pop()	       : Removes the element with the specified key
update()    	  : Updates the dictionary with the specified key-value pairs
popitem()	       : Removes the last inserted key-value pair
values()	       : Returns a list of all the values in the dictionary
setdefault()     : Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
'''

