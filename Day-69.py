#HCF of 2 numbers using recursion
def hcf(n1,n2):
    rem = n1 %n2
    if rem == 0:
        return n2
    res = hcf(n2,rem)
    return res

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
res =hcf(a,b)
print("HCF od",a,"and",b,"is",res)
