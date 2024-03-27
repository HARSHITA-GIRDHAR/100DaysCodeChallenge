# Multiplication table of a number
#programs with loops
num=int(input("Enter a number:"))
print("Multiplication table of",num,"is")
for n in range(1,11):
    result=n*num
    print(num,"x",n,"=",result)
    