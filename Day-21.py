# Sum of n natural numbers and printing sum of series
n=int(input("Enter n:"))
s=0
for a in range(1,n+1):
    s += 1/a
print("Sum is",s)