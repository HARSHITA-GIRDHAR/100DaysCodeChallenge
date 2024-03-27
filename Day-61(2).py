f=open("story.txt","r")
data = f.read()
print(data)

vowels = 0
for ch in data:
    if ch in "aeiouAEIOU":
        vowels += 1
print("No.of vowels is",vowels)
f.close()
