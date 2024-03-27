# List of armstrong numbers
for num in range(1000,9999):
    a = num
    s=0
    while a > 0:
        d = a % 10
        s = s + d ** 4
        a = a // 10
    if s == num:
        print(num,"is Armstrong number")
    