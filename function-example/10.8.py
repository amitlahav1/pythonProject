def prime_num(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
         return True



num=int(input("enter number:"))
if prime_num(num):
    print("prime")
else:
    print("not prime")
