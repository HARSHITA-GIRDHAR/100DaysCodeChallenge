#Validate name entered by user
def isValidName(name):
    for ch in name:
         if not (ch.isalpha() or ch ==' '):
            return False
    else:
            return True
txt = input("Enter the name to validate:")
if isValidName(txt):
    print(txt + "is a valid name")
else:
    print(txt + "is not a valid name")
    