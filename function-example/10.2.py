def sum_list(list):
    return sum(list)


list=[]
num=int(input("how many number you want in the list?"))
for i in range(num):
    num2 = int(input("enter another number to your list:"))
    list.append(num2)


print("the list is:", list)
print("the sum of list is:", sum_list(list))


