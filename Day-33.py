# Guess the number
import random
num=random.randint(10,50)
for i in range(5):
     guess=int(input("Enter a number between 10 to 60:"))
     if guess == num:
         print("*" * 20)
         print("     YOU WIN!")
         print("*" * 20)
         break
     elif num > guess:
         print("Sorry ,but the number is greater than your guess \n")
     elif num < guess:
         print("Sorry ,but the number is lesser than your guess \n")
else:
         print("`" * 20)
         print("     YOU LOOSE!")
         print("`" * 20)
         