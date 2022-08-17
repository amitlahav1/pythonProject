num=int(input("enter number:"))
minnum=0
while num>0 or num<0:
    if(minnum==0):
        minnum=num
        continue
    minnum=min(num,minnum)
    num = int(input("enter number:"))

print((minnum),"this the min number")