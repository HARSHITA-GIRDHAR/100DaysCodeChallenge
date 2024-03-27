#check strength of the password
password = input("Enter the required password :")
n=len(password)
if n >=8 and n <= 16:
    c=0 #counter for capital letters 
    s=0 #counter for small letters
    d=0#counter for digits
    b=0#counter for special symbols
    a=0#counter for other characters which are not allowed in password
    for ch in password:
        if ch.isupper():
            c += 1
        elif ch.islower():
            s += 1
        elif ch.isdigit():
            d += 1
        elif ch in ",.:;&/\$@()~><":
            b += 1
        else:
            a += 1
            break
        if a!= 0:
            print("Invalid password!")
        else:
            if c >0 and s >0 and d >0 and b >0:
                print("Password strength is strong")
            else:
                ("Weak Password")
else:
    print("Password must have minimum of 8 characyers and maximum 16")

                