# Count the frequency of each letter in a string
txt=input("Enter a string:")
d={}
for ch in txt:
    if ch  not in d:
        d[ch]=1
    else:
        d[ch] += 1
print(d)
