def find_my(list1,num,num2=0):
    for i in range (len(list1)):
        if num in list1:
            return list1.index(num)


list=[2,4,3,1,2,6,7,44,5,3,2]
num=44
print(find_my(list,num))