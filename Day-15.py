#Prime number or not
num=int(input("Enter a number:"))
f=0
for a in range(1,num+1):
    if num % a==0:
        f +=1
if f==2:
    print(num,"is a prime number")
else:
     print(num,"is not a prime number")   
     