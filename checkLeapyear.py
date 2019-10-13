def checkLeapyear(year):
    if (year % 100) != 0 and (year % 4) == 0 or (year % 400) == 0:
        print("Year is a leap year")
    else:
        print("Year is not a leap year")


year = int(input("Enter the year : "))
checkLeapyear(year)
