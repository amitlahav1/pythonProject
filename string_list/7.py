from random import randint
list1=[]
num=randint(1, 10)
for i in range(10):
    list1.append(num)
    num = randint(1, 10)
print(f"original list: {list1}")

for i in range(len(list1)):
    if i%2!=0:

