
'''
_________________________________________________________________________________________________
==================================Nested Dictionary==============================================
=================================================================================================

=> Nested dictionary means putting a dictionary inside another dicionary
'''

course = {'php': {'Duration': '2 Month', 'Fees': '15000'},
          'python': {'Duration': '6 Month', 'Fees': '20000'},
          'JAVA': {'Duration': '12 Month', 'Fees': '18000'}
          }

for a,b in course.items():
    print(f"\n{a}  :  {b}")



print("\nAccessing nested dictionary : \n")
print(course['php']['Duration'])
print(course['php'].get('Fees'))



print("\nIterating Nested dictionary : \n")
for a,b in course['python'].items():
    print(f"{a}  :  {b}")




