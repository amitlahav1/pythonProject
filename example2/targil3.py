num=int(input("enter number: "))
sum1=int(num//100)
sum2=int(num//10%10)
sum3=int(num%10)
sumnumbers=(sum1+sum3+sum3)

if num>99 and num<=999:
    print(sumnumbers)
else:print("false")

