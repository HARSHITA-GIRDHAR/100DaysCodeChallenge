# Toggle case a string
txt=input("Enter a string:")
result = ""
for ch in txt:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch
print("Original string:",txt)
print("Resultant string:",result)
