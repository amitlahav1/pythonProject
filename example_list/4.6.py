# list1=[]
# for i in range(1,11):
#     list1.append(i)
# print(list1)
#
# #a
#
# print(list1[-3:])
# #b
# print(list1[::-1])
# #c
# # 1 2 3 4 5 6 7 8 9 10 numbers
# # 0 1 2 3 4 5 6 7 8  9  intex need to print
# for i in range (0,len(list1), 2):
#     print(list1[i])
#     #d
#
# odd=[]
# for i in list1:
#     if i%2!=0:
#         odd.append(i)
#
# print(odd)
#
#
# num=int(input("enter number:"))
# num2=int(input("enter number:"))
# num3=int(input("enter number:"))
# list1[4:5]=[num,num2]
# list1[-1]=[num3]
# print(list1)

#f
list1=[]
for i in range(1,11):
    list1.append(i)
print(list1)
for i in range(len(list1)):
    list1[i]*=2
print(list1)
#g

list1=list1[0],list1[-1]
print(list1)