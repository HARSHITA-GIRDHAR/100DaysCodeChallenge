#Creating a dictionary for employee
num = int(input("Enter the number of employees whose data to be stored: "))
count = 1
employee = dict() 
while count <= num:
 name = input("Enter the name of the Employee: ")
 salary = int(input("Enter the salary: "))
 employee[name] = salary
 count += 1
print("\n\nEMPLOYEE_NAME\tSALARY")
for k in employee:
 print(k,'\t\t',employee[k])
 