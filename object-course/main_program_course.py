from Student import Student
from Course import Course

number_course=input("enter number of course:")
name_course=input("enter name of course:")
max_students=input("enter number of max students:")

Course1=Course(number_course,name_course,max_students)

subject=input("enter a subject1:")
teacher=input("enter name of teacher:")

subject2=input("enter a subject 2 :")
teacher2=input("enter name of teacher:")



Course1.dic_subject_teacher.update({subject:teacher,subject2:teacher2})
id_student=int(input("enter ID of student(press 0 to stop):"))
while id_student!=0 :
    name_student=input("enter name of student:")
    age=int(input("enter age:"))
    student1 = Student(id_student, name_student, age)
    grade1=int(input(f"enter grade to {subject}"))
    grade2=int(input(f"enter grade to {subject2}"))
    student1.add_grade(subject,grade1)
    student1.add_grade(subject,grade2)

    if not Course1.add_student(student1):
        break
        print("the course canot to add this student, sorry ")
    id_student = int(input("enter ID of student(press 0 to stop):"))
print(Course1)

factor_subject=input("enter subject for factor:")
factor_Percent=int(input("enter factor in Percent : "))
Course1.add_factot(factor_subject,factor_Percent)

for index in Course1.weak_studnts():
    student = Course1.list_students[index]
    Course1.del_student(student)

print(Course1)
list_min_avg=Course1.weak_studnts()
list_weak_student=[]
for i in list_min_avg:
    list_weak_student.append(Course1.list_students)
print(list_weak_student, "weak student")
print(Course1)

print("oldest student", max(Course1.list_students))


