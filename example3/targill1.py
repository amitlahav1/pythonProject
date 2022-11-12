list1=[]
grade=int(input("enter grade:"))
sum_grade=0
while grade>=0 and grade<=100:

    list1.append(grade)
    sum_grade+=1
    grade = int(input("enter grade:"))

print(list1)

print(f" this the nax grde: {max(list1)}")
print(f" this the averge :{sum(list1)/sum_grade}")
print(max(list1)-sum(list1)/sum_grade)


