
list1=[]
from random import randint
num=randint(1,100)

for i in range(10):
    list1.append(num)
    num=randint(1, 100)

print(*list1)


