from random import randint
list1=[]
num=randint(1, 10)
for i in range(10):
    list1.append(num)
    num = randint(1, 10)
print(f"original list: {list1}")

#כל מה שמתחלק ב 3 למחוק
list2=[]
for i in range(len(list1)):
    if list1[i]%3!=0:
       list2.append(list1[i])



print(list2)
