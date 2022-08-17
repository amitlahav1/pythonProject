num=int(input("enter number:"))
while 99<num<=999:
    sum1 = int(num // 100)
    sum2 = int(num // 10 % 10)
    sum3 = int(num % 10)
    sum4 = (sum1 + sum3 + sum3)
    print(sum4)
    num = int(input("enter number again:"))

print("fail")
