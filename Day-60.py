#Login Screen
for k in range(3):
    userid = input("Enter the userid :")
    passw = input("Enter the password:")
    
    if userid.lower() == "harshita" and passw.lower() == "python":
        print("Password matched !!!")
        print("Access Granted")
        break
    else:
        print("Invalid user ID or Password")
else:
    print("Access denied")
    