world=input("enter world:")
world2=input("enter world:")
list1=""


for i in world:
    if i in world2 and i not in list1:
        list1+=i

print(list1)
print(len(list1))
