# Swap Adjacent Elements
A = eval(input("Enter the list of values:"))
print("Before Swap",A)
for i in range(0, len(A) ,2):
        temp=A[i]
        A[i] =A[i+1]
        A[i+1]=temp
print("After Swap",A)
