'''
_________________________________________________________________________________________________
================================DateTime Module Functions==========================================
=================================================================================================

now() : Return current time

strftime() : Takes one speific formate of parameter to return specified string

%b -> Month name in short version
%B -> Month name in full version
%m -> Month in Digit formate
%y -> Year without century
%Y -> Year with century
%H -> 24 hour formate
%I -> 12 hour formate
%p -> AM/PM
%M -> Minutes
%S -> Seconds
'''


import datetime as d


#datetime is an object inside datetime module
x=d.datetime.now()            
print(f"\nCurrent Time : {x}")


# Print in date formate yyyy-mm-dd 
x=d.datetime(2002,10,13)
print(f"\nDate Formate : {x}")



# Printing Using strftime() and their formate
x=d.datetime.now()




# Month Formates_________________________________________________________________________________________________
Short_month=x.strftime('%b')
Full_month=x.strftime('%B')
Digit_month=x.strftime('%m')

print(f"\n\nMonth printing forms : \nShort_version : {Short_month}\nFull_version : {Full_month}\nDigit_version : {Digit_month}")
#________________________________________________________________________________________________________________________






# Year Formates_________________________________________________________________________________________________
Short_year=x.strftime('%y')
Full_year=x.strftime('%Y')

print(f"\n\nYear printing forms : \nShort_version : {Short_year}\nFull_version : {Full_year}")
#________________________________________________________________________________________________________________________





# Hour Formates_________________________________________________________________________________________________
Hour24_formate=x.strftime('%H')
Hour12_formate=x.strftime('%I')

print(f"\n\nHour printing forms : \n24 Hour_version : {Hour24_formate}\n12 Hour_version : {Hour12_formate}")
#________________________________________________________________________________________________________________________




# AM PM Printing_______________________________________________________________________________________________________
AmPm=x.strftime('%p')
print(f"\nAM PM printing : \nAM or PM : {AmPm}")
#________________________________________________________________________________________________________________________




# Minutes Printing_______________________________________________________________________________________________________
minutes=x.strftime('%M')
print(f"\nMinutes : {minutes}")
# _________________________________________________________________________________________________



# Seconds Printing_______________________________________________________________________________________________________
seconds=x.strftime('%S')
print(f"\nSeconds : {seconds}")
# _________________________________________________________________________________________________

