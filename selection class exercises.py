#Ricky Santos
#selection class exercises improvments
#30/9/2014

day = int(input("please enter a day as a number between 1 - 31: "))
month = int(input("Please enter a month as a number between 1-12: "))
year = int(input("please entre the last two numbers of the year"))

if day == 1 or day == 21 or day == 31:
    day_after == "st"
if day == 2 or day == 22:
    day_after == "nd"
if day == 3 or day == 23:
    day_after == "rd"
else:
    day_after == "th"

if month == 1:
    month = "January"
elif month == 2:
    month = "February"
elif month == 3:
    print"March"
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

