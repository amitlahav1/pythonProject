world=input("enter world:")
j=""
count=-1
list0=[]
list1=[]
for i in world:
   count+=1
   list0.append(i)
   if i in list0[0:count]:
       list1.append(i)

print("".join(list1))





