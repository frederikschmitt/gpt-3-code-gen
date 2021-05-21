year = int(input("Enter year: "))
leap = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    else:
        leap = True
if leap:
    print(f"Year {year} is a leap year.")
else:
    print(f"Year {year} is not a leap year.")