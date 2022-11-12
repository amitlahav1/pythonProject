list1=[]
from random import randint
num=randint(0,8888888)

for i in range(10):
    list1.append(num)
    num = randint(0, 8888888)

print(list1)

