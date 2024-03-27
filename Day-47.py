# Union & Intersection of two lists in python
A=eval(input("Enter list 1"))
B=eval(input("Enter list 2"))

U=A.copy()
I=[]
for val in B:
    if val in A:
        I.append(val)
    else:
        U.append(val)
print(A)
print(B)
print(U)
print(I)