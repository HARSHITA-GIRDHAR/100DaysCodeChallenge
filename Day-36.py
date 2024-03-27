#Reversing a List
A=eval(input("Enter list of values:"))
n=len(A)
for i in range( n//2):
    A[i],A[n-1-i] = A[n-1-i],A[i]
print(A)
