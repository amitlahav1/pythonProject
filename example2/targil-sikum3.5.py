num=int(input("how many numbers you want?"))
n1=0
n2=0
count=0

if num <=0:
    print ("enter positive number")
elif num ==1:
    print("fibonachi" , num)
    print(n1)
else:
    print("fibonachi:")
    while count<num:
        print(n1)
        fibo=n1+n2
        n1=n2
        n2=fibo
        count+=1
