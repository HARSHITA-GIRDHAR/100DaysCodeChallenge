# No. of vowels in a string
txt = input("Enter a string:")
c=0
for ch in txt:
    if ch in 'aeiouAEIOU':
        c+=1
print("No.of vowels",c)
