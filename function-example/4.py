def my_max (list1):
    count=0
    for i in list1:
        count1=i
        if i>count1:
            count+=i
            continue

    return count


list1=[2,4,3,2,11,22,3,11,4,55,33,11,3]
print(my_max(list1))