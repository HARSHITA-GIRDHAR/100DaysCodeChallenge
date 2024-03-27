# Check if an emil id is valid or not
email=input("Enter email-id:")

if email.endswith(".com"):
    if email[0] != '@' and  email.count("@") ==1:
        for ch in email:
          if ch.isalpha() or ch.isdigit() or ch=="." or ch=="_" or ch=="@":
            continue
          else:
            print("Not a valid email-id")
            break
        else:       
          print("Valid email-id")
    else:
     print("Not a Valid email-id")
else:
    print("Not a Valid email-id")
