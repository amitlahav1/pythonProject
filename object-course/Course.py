from Student import Student

class Course:
        def __init__(self,number_course,name_course,max_students):
            if type(number_course)!=int:
                raise TypeError ("number of course must to be type int !!!!")
            if number_course<0:
                number_course=0
            if type(name_course)!=str:
                raise TypeError("name of course must to be type str !!!!")
            if type(max_students)!=int:
                raise TypeError("max students must to be type int !!!!!")
            if max_students<0:
                max_students=20

            self.number_course=number_course
            self.name_course=name_course
            self.max_students=int(max_students)
            self.dic_subject_teacher={}
            self.list_students=[]

        def __str__(self):
            return f"number of course:{self.name_course}, name of coursr:{self.name_course},max students:{self.max_students}\nlist of the students:{self.list_students}\nlist of subject:teacher:{self.dic_subject_teacher}"


        def add_student(self,name):
            if len(self.list_students)<self.max_students:
                self.list_students.append(name)
                return True
            else:
                False

        def add_factot(self,subject,factor_Percent):
            if type(factor_Percent)!=int:
                raise TypeError("factor must to be type int !!!!!")
            if subject not in self.dic_subject_teacher:
                print(f"{subject} not exist in subject list")
                return
            for student in self.list_students:
                student.calc_factor(subject,factor_Percent)

        def del_student(self,object_student:Student):
            if object_student not in self.list_students:
                print (f"the student {object_student} not in the course.")
                return
            else:
                self.list_students.remove(object_student)


        def averages(self):
            list_average=[]
            for student in self.list_students:
                list_average.append(student.averge())
            return list_average


        def weak_studnts(self):
            list_avg=self.averages()
            list_index=[]
            index_st=0
            min_avg=min(list_avg)
            for i in range(list_avg.count(min_avg)):
                index_st=list_avg.index(min_avg,index_st)
                list_index.append(index_st)
                index_st+=1
            return list_index

# add a lettter






























