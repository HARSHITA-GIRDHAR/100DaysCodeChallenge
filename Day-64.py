# Contact book using binary files
import pickle
import os
def addContact():
    name=input("Enter your name:")
    phone=input("Enter your phone number:")
    data =[name,phone]
    f=open("contacts.dat","ab")
    pickle.dump(data,f)
    f.close()
    print("Added successfully")

def display():
    f=open("contacts.dat","rb")
    print("-" * 30) 
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            print(data[0] +"\t\t"+data[1])
    except:
        f.close()
def search():
    name=input("Enter name to be searched:")
    f=open("contacts.dat","rb")
    print("-" * 30) 
    n=0
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
               print(data[0] +"\t\t"+data[1])
               n += 1 
    except:
        if n == 0:
            print("No such contact found")
        f.close()
def update(): 
    name=input("Enter name to be updated:")
    f=open("contacts.dat","rb")
    g=open("temp.dat","wb")
    print("-" * 30) 
    n=0
    print("Name\t\tContact")
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
               print(data[0] +"\t\t"+data[1])
               phone=input("Enter the modified phone number:")
               data[1]=phone
               n += 1 
            pickle.dump(data,g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("No such contact found")
        else:
            os.remove("contacts.dat")
            os.rename("temp.dat","contacts.dat")
        f.close()
def delete(): 
    name=input("Enter name to be deleted:")
    f=open("contacts.dat","rb")
    g=open("temp.dat","wb")
    print("-" * 30) 
    n=0
  
    try:
        while True:
            data = pickle.load(f)
            if data[0] == name:
               print("Deleted record"+data[0] +"\t\t"+data[1])
               n +=1
            else:
               pickle.dump(data,g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("No such contact found")
        else:
            os.remove("contacts.dat")
            os.rename("temp.dat","contacts.dat")
        f.close()
while True:
    print("-" * 30) 
    print("Press 1 - Add a new contact")
    print("Press 2 - Display all contacts")
    print("Press 3 - Search a contact")
    print("Press 4 - Update a  contact")
    print("Press 5 - Delete a  contact")
    print("Press any other number to exit")
    print("-" * 30)
    choice=int(input("Enter your choice:"))
    if choice == 1:
        addContact()
    elif choice ==2:
        display()
    elif choice ==3:
        Search()
    elif choice ==4:
        Update()
    elif choice ==5:
        delete()
    else:
        break
    