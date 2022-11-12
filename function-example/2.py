def my_count(list1,num):
    count=0
    for i in list1:
        if num in list1:
            count+=1
            list1.remove(i)

    return count

num=3
list2=[3,2,3,4]
print(my_count(list2,num))