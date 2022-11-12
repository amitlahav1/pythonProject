world=input("enter world:")
world2=input("enter world:")
list=[]
world.split()
world2.split()

for i in world:
    if i in world2 and i not in list:
        list.append(i)

        print(list)