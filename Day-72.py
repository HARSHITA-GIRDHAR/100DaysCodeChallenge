#automorphic number or not
num=int(input("Enter a number:"))
sq=num**2
print("Square is",sq)

n=len(str(num))
end=sq%10**n

if end == num:
    print("Automorphic number")
else:
    print("Not an automorphic number")