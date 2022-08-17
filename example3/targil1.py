num=int(input("enter number :"))
for i in range (2,num):

     if num%i==0:
         print("not prime number")
         num = int(input("enter number :"))

else:
    print("prime number!")
