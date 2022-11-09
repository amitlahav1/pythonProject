def list_numbers (num1,num2):
    list1=[]
    for i in range(num2,num1+1):
        list1.append(i)


    print(list1)


def max_number (num,num2):
    list1=[num,num2]
    return max(list1)



def min_number (num,num2):
    list1=[num,num2]
    return min(list1)








num1=int(input("enter number:"))
num2=int(input("enter number:"))

list_numbers(max(num1,num2),min_number(num2,num1))

