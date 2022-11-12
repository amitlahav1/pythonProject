from unittest import TestCase
from Course import Course
from Student import Student

class TestCourse(TestCase):
    def setUp(self):
        self.student_1=Student(123,"amit",22)
        self.student_2=Student(12,"yosi",22)
        self.course_1=Course(1,"qa",10)

#add student to list. valid
    def test_add_student_valid1(self):
        self.course_1.list_students=["amit","yosi"]
        self.course_1.add_student("stav")
        self.assertEqual(self.course_1.list_students,["amit","yosi","stav"])
        self.assertTrue(self.course_1.list_students)

#add student to full list. invalid
    def test_add_student_invalid1(self):
        course=Course(1,"qa",3)
        course.list_students=["pa","pc","pd"]
        course.add_student("amit")
        self.assertEqual(course.list_students,["pa","pc","pd"])
        self.assertFalse(course.add_student("amit"))
        print(course.list_students)

#add factor to all student
    def test_add_factot_valid(self):
        self.student_1.dic1={"qa":80,"am":90}
        self.student_2.dic1={"qa":82,"am":92}
        # self.course_1.list_students=[self.student_1,self.student_2]
        # print(self.course_1.list_students)
        self.course_1.dic_subject_teacher={"qa":"orly"}
        self.course_1.add_factot("qa",10)
        self.course_1.add_student(self.student_1)
        self.course_1.add_student(self.student_2)
        self.course_1.add_factot("qa",10)
        print(self.course_1.list_students)



















    def test_del_student(self):
        self.fail()

    def test_averages(self):
        self.fail()

    def test_weak_studnts(self):
        self.fail()
