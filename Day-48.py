# Cartesian product of two lists
A = eval(input("Enter the elements of first list:"))
B = eval(input("Enter the elements of second list:"))

R = []
for n1 in A:
    for n2 in B:
        R.append((n1,n2))
print(A)
print(B)
print(R)