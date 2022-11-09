class Coures:
    def __init__(self,num_couers,name_coures,registered_student,max_student):
        self.number= num_couers
        self.name=name_coures
        self.registered=registered_student
        self.max_student=max_student

    def place_coures(self):
        place=self.max_student-self.registered
        return place

    def new_students(self,new_student):
        if new_student<=self.place_coures():
            self.registered+=new_student
        else:
            sum1=new_student-self.place_coures()
            sum2=new_student-sum1
            self.registered+=sum2

    def __str__(self):
        return (f"the number of students: {self.number} the name: {self.name} the registered:{self.registered} the max:{self.max_student}")



number_coures=int(input("enter number of the coures:"))
name_coures=input("enter name of coures:")
number_student=int(input("enter number of the students:"))
max_students=int(input("enter a max students:"))

couers1=Coures(number_coures,name_coures,number_student,max_students)
print(couers1)

new_student=int(input("enter hoe many new students:"))
couers1.new_students(new_student)
print(couers1)
