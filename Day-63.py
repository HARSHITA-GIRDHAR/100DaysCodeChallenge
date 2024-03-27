import csv
uname =input("Enter username:")
passw= input("Enter password :")

f=open("Day-63.csv","r")
cr= csv.reader(f)
for row in cr:
    if row[0]==uname and row[1]==passw:
        print("Welcome",uname,"access granted")
        break
else:
    print("Invalid Username or password")

f.close()