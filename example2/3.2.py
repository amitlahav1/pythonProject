num=int(input("enter number:"))
flag=False

if num > 1:
    for i in range(2, num):
        flag=True
        break

    if flag:
        print ("not prime")
    else:
        print("prime")
else:
    print("not prime")


