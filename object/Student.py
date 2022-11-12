class Student:
    def __init__(self,id,name,grade):
        self.id=id
        self.name=name
        self.grade=grade

    def checkpass(self, grade):
         if grade>70:
            return True
         if grade<70:
            return False

    def updategrade(self, factor,grade):
        sum_factor=grade*factor/100
        sum_grade=sum_factor+grade
        if sum_grade>=100:
             self.grade=100

        else:
            self.grade=sum_grade

    def __str__(self):
        return (f"the id is:{self.id}, the name is:{self.name}, the grade is:{self.grade}")


id=input("enter id:")
name=input("enter name:")
grade=int(input("enter grade:"))

student1=Student(id,name,grade)
print(student1)

if student1.checkpass(grade):
    print("pass")
else:
    print("not pass")


factor=int(input("enter factor in %:"))
student1.updategrade(factor,grade)
print(student1)

