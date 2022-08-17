num=int(input("enter number:"))
sum=0


while num>0 or num<0:
    if num%7==0 or num%3==0:
        sum+=1


    num=int(input("enter number:"))

print(sum)

