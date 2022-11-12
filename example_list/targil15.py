def grades_number(number):
    list_grades = {}

    for i in range(1, number+1):
        grade = int(input("enter grade:"))
        list_grades.update({i: grade})

    return (list_grades)

def avrage_grades(list1) :
    list2=list1.values()
    sum1=sum(list2)
    sum2=len(list2)
    averge1=sum1/sum2
    return averge1



num=int(input("enter number of students:"))
list1=grades_number(num)

print(list1,"this the list of grades!")
print("the averge is:", avrage_grades(list1))

