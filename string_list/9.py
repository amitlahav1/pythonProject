from random import randint
list1=[]
num=randint(1, 10)
for i in range(10):
    list1.append(num)
    num = randint(1, 10)
print(f"original list: {list1}")



num=int(input("enter number :"))
#להכניס את המספר שנקלט במקום אינדקסים 7-9
list1[-3:]=[num]
print(list1)