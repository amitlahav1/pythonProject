grade=int(input("enter grade 1-100:"))

list1=[]
sum_succses=0
sum_faild=0
while grade>=1 and grade<=100:
    list1.append(grade)

    if grade>=60:
        sum_succses+=1
    else:
        sum_faild+=1
    grade = int(input("enter grade 1-100:"))

print("faild:", sum_faild)
print("succses:", sum_succses)

print (list1)


