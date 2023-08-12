'''
# ========================================JSON Module==============================================

JSON -> (Java Script Object Notation)

=> It is mainly used for the Transferring data between the browser and the server.

ex: API's using between servers and browser or application to Represent data. Those API are only understood Json notation formate.
So, Json is a 'text formate' that is used for data exchange between (SERVER & BROWSER) , (SERVER & APPLICATIONS)

=> python also supports Json with built in json module.



=====================================================================================================
******************************************** J S O N ************************************************
========================================Supported Datatypes==========================================
=====================================================================================================

Json supports mainly 6 type of datatypes:
(1) String
(2) Number
(3) Boolean
(4) Null
(5) Onjects
(6) Array

--> In python json exist as a string

example : p='{"Name":"Yash" , "Language":["Python","JAVA"]}'




====================================================================================================
===============================================Json Methods=========================================
====================================================================================================
dumps(obj) : convert data into json string formate
load() : Reconvert Json string into Default Datatype formate

'''

import json



d = {"Name": "Yash", "Course": "Python", "Fees": 2500}


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("\n-> Using dumps() to convert data into Json Formate")
print(f"\nGiven Data : {d}")
print(type(d))


f=json.dumps(d)
print(f"\nConverted Json String : {f}")
print(type(f))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# If we have a Json String the with te help of load() we can convert it into actual python supportes formate
# We Have Json String In Variable 'f'
print("\n-> Using Loads() to convert Json String into Data")

print(f"\nGiven Json String : {f}")
print(type(f))

y=json.loads(f)
print(f"\nConverted Data : ")
for k,v in y.items():
    print(f"{k} : {v}")

print(type(y))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


