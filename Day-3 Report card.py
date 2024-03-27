#print student's report card
name=input("Enter name:")
maths=float(input("Enter marks in maths:"))
english=float(input("Enter marks in english:"))
science=float(input("Enter marks in science:"))
hindi=float(input("Enter marks in hindi:"))
sst=float(input("Enter marks in sst:"))
total=maths+english+science+hindi+sst
percentage=total/5
print("----------------------")
print("Report card for",name)
print("------------------")
print("Total marks scored",total)
print("percentage marks",percentage,"%")
if percentage>=40:
    print("Congratulations!!!")
else:
    print("Try again")
print("------------")

