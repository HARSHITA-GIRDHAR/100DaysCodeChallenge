#String Palindrome
txt=input("Enter a string:")
rev = txt[::-1]
print("String is",txt)
print("Reverse is",rev)
if txt == rev:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
    