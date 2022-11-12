num=int(input("enter num:"))
list=[]
for i in range (7):
    list.append(num)
    num = int(input("enter num:"))

print(max(list))