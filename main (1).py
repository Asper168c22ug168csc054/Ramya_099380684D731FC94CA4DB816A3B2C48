Year=int(input("Enter year:"))
if year % 4==0 and year % 100 !=0:
    Print(year, "is Leap year")
elif year % 100==0:
    Print(year, "is not a leap year")
elif year %400==0:
    Print(year, "is a leap year")
else:
    Print(year, "is not a leap year")