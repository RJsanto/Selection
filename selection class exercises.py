#Ricky Santos
#selection class exercises improvments
#2/10/2014

import time

while True:

####################################

    century = int(input("please select your century; 20th or 21st: "))

    if century == 20:
        century = 1900
    elif century == 21:
        century = 2000
    else:
        print ("That is an invalid century for this program")


    day = int(input("please enter a day as a number between 1 - 31: "))
    day_suffix = day

    if day_suffix == 1 or day_suffix == 21 or day_suffix == 31:
        day_suffix = "st"
    elif day_suffix == 2 or day_suffix == 22:
        day_suffix = "nd"
    elif day_suffix == 3 or day_suffix == 23:
        day_suffix = "rd"
    else:
        day_suffix = "th"


    month = int(input("Please enter a month as a number between 1-12: "))
    month1 = month

    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == 11:
        month = "November"
    elif month == 12:
        month = "December"
    else:
        print ("there isn't that many months in the year")


    year = int(input("please entre the last two numbers of the year: "))
    leapyear = "posible"

    if  (year % 200) == 0 and (year%4) == 0:
        leapyear = "this is a leap year"
    else:
        leapyear = "this is not a leap year"



    year2 = century + year


    if  (year2 % 200) == 0 and (year2 % 4) == 0:
        leapyear = "this is a leap year"
    else:
        leapyear = "this is not a leap year"


    print ("{0},{1}{2},{3}".format(month,day,day_suffix,year2))
    print (leapyear)

#########################################

    endProgram =  input("Do you wish to end the program? (Enter no to process a new set of dates): ")

    time.sleep (2)
    
    if endProgram == "yes":
        break
