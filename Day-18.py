# Fibonaaci Series
n=int(input("How many elements of fibonaaci series are to be printed:"))
a=0
b=1
for i in range(n):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
