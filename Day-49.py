# Rotate a list by n positions
A=eval (input("enter the list elements:"))
n=int(input("enter the number of positions to be shifted:"))
print(A)
for i in range(n):
    temp = A[0]
    for j in range(len(A)-1):
        A[j]=A[j+1]
    A[-1]=temp
    print(A)
    
