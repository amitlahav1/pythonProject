def sum_list (list):
    result=1
    for i in list:
        result=result*i
    return result










list=[]
num=int(input("how many number you want in the list?"))
for i in range(num):
    num2 = int(input("enter another number to your list:"))
    list.append(num2)
print(list)

print(sum_list(list))