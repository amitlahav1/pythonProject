class Student:
    def __init__(self,id1,name,age):
        if type(id1)!=int:
            raise TypeError("id must to be type int  !!!!")
        if type(name)!=str:
            raise TypeError("name must to be type str !!!!")
        if type(age)!=int:
            raise TypeError("age must to be type int !!!!")
        if id1<=0:
            raise ValueError("id must be >0 !!!")
        if age<0 or age>120:
            age=0

        self.id1=id1
        self.name=name
        self.age=age
        self.dic1={}

    def add_grade(self,subject_study,grade):
        if type(grade)!=int:
            raise TypeError("grade must to be type int !!!!")
        if grade<0:
            grade=0
        if grade>100:
            grade=100

        self.dic1[subject_study]=grade


    def __str__(self):
        return f"name:{self.name} age:{self.age} id:{self.id1} list-subject of study and grade:{self.dic1}"

    def __repr__(self):
        return f"{self.id1} {self.name} age:{self.age} {self.dic1}"

    def calc_factor(self,subject_study,factor_Percent):
        if subject_study not in self.dic1:
            print(f"{subject_study} not in grades list.")
            return
        if type(factor_Percent)!=int:
            raise TypeError("factor must be type int !!!!")
        self.dic1[subject_study]+=self.dic1[subject_study]*factor_Percent/100
        if self.dic1[subject_study]>100:
            self.dic1[subject_study]=100

    def averge(self):
        list_grade=self.dic1.values()
        list_grade_sum=sum(list_grade)
        len_list_grade=len(list_grade)
        averge=list_grade_sum/len_list_grade
        return averge

    def __eq__(self, other):
        if self.id1 == other.id1:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.age > other.age:
            return True
        else:
            return False






