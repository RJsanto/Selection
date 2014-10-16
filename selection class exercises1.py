day = int(input("please enter a day as a number between 1 - 31: "))

day_suffix = day

if day_suffix == 21 or day_suffix == 1:
    day_suffix = "st"

print (day)
print (day_suffix)
