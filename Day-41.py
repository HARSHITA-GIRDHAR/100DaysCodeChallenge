# Selection sort
a=eval(input("enter the list of numbers:"))
n=len(a)
print("before swap",a)
for i in range(n-1):
    for j in range(i+1,n):
        if a[i] > a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("After swap",a)

