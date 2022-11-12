def list (num1,num2):
    list1=[]
    for i in range(num2,num1+1):
        list1.append(i)


    print(list1)


num1=int(input("enter number:"))
num2=int(input("enter number:"))
list(num1,num2)
