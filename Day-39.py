# Removing duplicates from a list
A = eval(input("Enter a list of values:"))
i=0
print("Before Remove list is",A)
while i < len(A):
    if A.count(A[i])>1:
        A.remove(A[i])
    else:
        i += 1
print("After remove list is",A)
