def list_up (list1):
    from random import randint
    num=randint(1,100)
    for i in range(20):
        list1.append(num)

        num = randint(1,100)

def sum_numbers (num,list1):
    count=0
    for i in range(len(list1)):
        if list1[i]==num:
            count+=1

        continue

    return count

list4=[]
list_up(list4)
print(list4)

num=int(input("enter number:"))

print(sum_numbers(num,list4),"-the time that your number show in this list")