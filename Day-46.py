#Reversing a string word to word
txt = input("Enter string to be reversed:")
words = txt.split()
words=words[::-1]
print(words)
result = " "
for w in words:
    result += w +" "
print(result)
