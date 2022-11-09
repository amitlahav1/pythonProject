

from random import  randint
num=randint(1,100)
list1=[]
for i in range(10):
    list1.append(num)
    num = randint(1, 100)
print(list1 ,"list")
t1=tuple(list1)
print("tuple:", t1)

num2=input("enter number , (to add):")
t1+=(num2,)
print(t1,"c")

t2=()
t2=t1[:4]+t1[-4:]

print(t2)


list3=[]
list3=list(t2)
list3[:1]=[]

t2=tuple(list3)

print(t2)