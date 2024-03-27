# LCM of two numbers
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if a>b:
    g=a
else:
    g=b
for n in range(g, a*b +1):
    if n % a==0 and n % b==0:
        print("LCM of ",a,"and",b,"is",n)
        break
    