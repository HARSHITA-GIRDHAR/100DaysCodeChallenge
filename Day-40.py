#Second highest value of a list
A = eval(input("Enter the list of values:"))
m=max(A)
while m in A:
    A.remove(m)
res=max(A)
print("second highest is",res)


