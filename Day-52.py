#Search and update a dictionary
def create(demp,n):
    for i in range(n):
        ename=input("Enter employee name:")
        sal=int(input("Enter the salary:"))
        demp[ename]=sal
def search(demp,name):
   if name in demp:
       demp[name]+=demp[name] * 25 /100
       print("Salary updated")
   else:
        print("No employee found with given name")       
demp={}
n=int(input("How many employees are there :"))
create (demp,n)
print("Dictionary is ",demp)
name=input("Enter employee name whose salary has to be increased :")
search(demp,name)
print("Dictionary is ",demp)
