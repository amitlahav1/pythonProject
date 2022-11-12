from random import randint
list1=[]
num=randint(1, 10)
for i in range(10):
    list1.append(num)
    num = randint(1, 10)
print(f"original list: {list1}")


#ממיקום 2 כל מיקום הבא יהיה סכום המספרים לפניו. 1ו 2 הם 1
count=0
list1[0:1]=[1]
list1[1:2]=[1]
print(list1)
for i in range(len(list1)):




# amount = int(input("enter how many numbers in fibonacci series (at least 2): "))
#
# num1=0
# num2=1
#
# print(num1,num2,end=' ')
# # 0 1 1 2
# for i in range(amount-2):
#     num3 = num1+num2
#     print(num3,end=' ')
#     num1=num2
#     num2=num3
