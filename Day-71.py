# Check if it is a strong number or not
import math
num=int(input("Enter a number:"))
s=0
a=num
while num>0:
    d=num %10
    s += math.factorial(d)
    num = num//10
    
if s == a:
    print("Strong number")
else:
    print("Not a Strong number")
    
