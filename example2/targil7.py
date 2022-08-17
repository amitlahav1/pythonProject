num=int(input("enter number:"))
sum=int(num//10%10)
sum2=int(num%10)
if num>=10 and num<100:
    if num%7==0 or sum==7  or sum2==7:
        print ("lucky number")
else:
    print ("invaild")

