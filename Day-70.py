# Sum of digits using recursion
def sumofdigit(num):
    if num == 0:
        return 0
    d=num %10
    num=num//10
    res= d+ sumofdigit(num)
    return res

n=int(input("Enter a number:"))
r=sumofdigit(n)
print("Sum of Digits of",n,"is",r)
