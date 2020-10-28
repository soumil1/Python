# Python program to check if year is a leap year or not

year = 2000

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} Leap Year".format(year))
       else:
           print("{0} not a Leap Year".format(year))
   else:
       print("{0}leap year".format(year))
else:
   print("{0} not a Leap Year".format(year))