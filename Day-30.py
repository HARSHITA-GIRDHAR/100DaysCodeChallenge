n=int(input("Enter number of rows:"))
for a in range(n,0,-1):
    for s in range(a):
        print("*",end=' ')
    for b in range(2*(n-a)):
        print(" ",end=' ')
    for s in range(a):
        print("*",end=' ')
    print()
for a in range(1,n+1):
    for s in range(a):
        print("*",end=' ')
    for b in range(2*(n-a)):
        print(" ",end=' ')
    for s in range(a):
        print("*",end=' ')
    print()
    