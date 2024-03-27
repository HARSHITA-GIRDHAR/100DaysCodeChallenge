# Check if a word has easy pronounciation or not
word=input("Enter a word:")
c=0
for ch in word:
    if ch.isalpha():
       if ch not in 'aeiouAEIOU':
           c += 1
           if c== 4:
               print("It is difficult to pronounce")
               break
       else:
            c=0
    else:
          print("Invalid input")
          break
else:
        print("It is easy to pronounce:")
         
               
           