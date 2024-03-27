# HCF of two numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
while a%b !=0:
    remainder=a%b
    a=b
    b=remainder
    
    print("HCF is",b)
    