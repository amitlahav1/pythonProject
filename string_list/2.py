from random import randint
list=[]
num=randint(1, 10)

for i in range(10):
    list.append(num)
    num = randint(1, 10)

print(list)