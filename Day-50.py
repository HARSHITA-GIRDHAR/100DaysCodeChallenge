# Print all combinations of three digits
A =[0,0,0]
A[0] = int(input("Enter first digit:"))
A[1] = int(input("Enter second digit:"))
A[2] = int(input("Enter third digit:"))

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j != k and k != i:
             print(A[i],A[j],A[k])
        