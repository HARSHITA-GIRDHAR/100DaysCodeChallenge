# Validate phone no. entered by user
def isPhoneValid(phone):
    if len(phone) != 10:
        return False
    elif not phone.isdigit():
        return False
    elif phone[0] not in ("789"):
        return False
    else:
        return True

txt=input("Enter phone number:")
if isPhoneValid(txt):
   print("Phone number is valid")
else:
    print("Phone number is not valid")   
    

