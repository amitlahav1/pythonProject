from random import randint
list=[]
num=randint(1, 100)

for i in range(10):
    list.append(num)
    num = randint(1, 100)

print(list)