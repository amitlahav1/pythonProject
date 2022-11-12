def grades_number(num):
    list_grades = []
    for i in range(num):
        list_grades.append(int(input("enter grade:")))
    return list_grades


num_students = int(input("enter number of students:"))
print(grades_number(num_students))
