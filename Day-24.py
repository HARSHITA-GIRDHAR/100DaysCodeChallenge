#List of prime numbers in a given range
start=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))

for num in range(start,end+1):
    for a in range(2,num):
        if num % a ==0:
            break
    else:
        print(num,"is a prime number")
        