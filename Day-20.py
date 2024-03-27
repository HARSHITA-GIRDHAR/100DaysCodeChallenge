# palindrome
num=int(input("Enter a number to be checked:"))
a=num
result=0
while a >0:
    d =a % 10
    result= result * 10 + d
    a = a // 10
if num == result:
    print(num, "is a Palindrome")
else:
    print(num, "is not a Palindrome")
