# Diamond
n=int(input("Enter number of rows:"))
for a in range(1,n+1):
     for s in range(n-a):
          print(" ",end=' ')
     for b in range(2 * a - 1):
          print("*",end=' ')
     print()
     
for a in range(n-1,0,-1):
     for s in range(n-a):
          print(" ",end=' ')
     for b in range(2 * a - 1):
          print("*",end=' ')
     print()
     