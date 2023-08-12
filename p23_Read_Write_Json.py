'''
We have a json text file and in this program we are try to read and write data in json file

It is much similar like a API brings data from the surver and we are try to convert it into editable formate
'''

import json



# Reading a json file after conversion
f=open("p23_jsonFile.json", "r+")
x = f.read()
data = json.loads(x)

for k, v in data.items():
    print(f"\n{k} : {v}")



