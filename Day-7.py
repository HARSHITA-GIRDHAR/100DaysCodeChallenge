#Leap Year or non leap year
year=int(input("Enter the year to be checked:"))
if year % 100 == 0:
    if year % 400 ==0:
        print(year,"is a leap year")
    else:
        print(year,"year is not a leap year")
else:
     if year%4 ==0:
         print(year,"is a leap year")
     else:
         print(year,"year is not a leap year")   
         

