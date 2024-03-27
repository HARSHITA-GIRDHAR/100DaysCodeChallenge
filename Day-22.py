# Sum of series
x=int(input("Enter value of x: "))
n=int(input("Enter value of n: "))
s=0
for a in range(1,n+1):
    if a<n:
       print(str(x),"^",str(a),end="+")
    else:
       print(str(x),"^",str(a))
    s += x ** a
    
print("Sum is",s)