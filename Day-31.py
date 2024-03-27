# Cross-pattern &Cross with a border using nested loops
#case-1
n=int(input("How many lines are there: "))
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b or a + b == n + 1 :
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
