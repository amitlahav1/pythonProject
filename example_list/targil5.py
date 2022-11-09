def sum_numbers (num1):
    list1=[]
    for i in range(1,num1+1):
        list1.append(i)
    return (sum(list1))



for i in range(5):
    num_user=int(input("enter number :"))
    print(sum_numbers(num_user))