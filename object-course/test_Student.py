from unittest import TestCase
from Student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student_valid=Student(123,'amit',22)

#test a valid case to __init__
    def test_init_valid_1(self):
        self.assertEqual(self.student_valid.id1,123)
        print(self.student_valid.id1)
    def test_valid_init2(self):
        self.assertEqual(self.student_valid.name,'amit')
    def test_nam_(self):
        self.assertEqual(self.student_valid.age,22)

#test to worng type in init.
    def test_init_invalid_argument_type(self):
        with self.assertRaises(TypeError):
            student1=Student('aa','amit',22)
        with self.assertRaises(TypeError):
            student2=Student(11,212,22)
        with self.assertRaises(ValueError):
            student3=Student(-11,'amit',22)

#test to invalid init - values
    def test_init_invalid_values(self):
        with self.assertRaises(ValueError):
            student3 = Student(-1, 'amit', 22)
            student4=Student(0,'ami',11)

#test to age<0 and age>120. defult=age=0
    def test_age_defult(self):
        p1=Student(12,'amit',-1)
        p2=Student(12,'amit',121)
        self.assertEqual(p1.age,0)
        self.assertEqual(p2.age,0)

#add a grade to subject
    def test_add_grade_valid_1(self):
        self.student_valid.add_grade("qa",80)
        self.assertEqual(self.student_valid.dic1,{"qa":80})

#add grade for exist subject
    def test_add_grade_exist_subject_valid_1(self):
        self.student_valid.dic1={"qa":80}
        self.student_valid.add_grade("qa",99)
        print(self.student_valid.dic1)
#add grade invalid-str
    def test_add_grade_invalid(self):
        with self.assertRaises(TypeError):
            self.student_valid.add_grade("qa",'asa')
            self.assertRaises(TypeError)

#add factor 10% , valid test
    def test_calc_factor_valid_1(self):
        self.student_valid.dic1={"qa":80}
        self.student_valid.calc_factor("qa",10)
        self.assertEqual(self.student_valid.dic1,{"qa":88})

#add factor that over grade 100- defult 100.
    def test_calc_factor_defult(self):
        self.student_valid.dic1 = {"qa": 90}
        self.student_valid.calc_factor("qa", 30)
        self.assertEqual(self.student_valid.dic1, {"qa": 100})

#add factor for 3 subject
    def test_calc_factor_valid_2(self):
        self.student_valid.dic1 = {"qa": 80,"qa": 60,"qa": 55}
        self.student_valid.calc_factor("qa", 10)
        self.assertEqual(self.student_valid.dic1, {"qa": 88,"qa": 66,"qa": 60.5})

#add factor for no exist subject
    def test_subject_invalid_(self):
            self.student_valid.dic1={"qa":80,"aa":89}
            self.student_valid.calc_factor("qq",10)
            self.assertEqual(self.student_valid.dic1,{"qa":80,"aa":89})

#add invalid factor.type str.
    def test_grade_invalid_type(self):
        with self.assertRaises(TypeError):
            self.student_valid.dic1 = {"qa": 80, "aa": 89}
            self.student_valid.calc_factor("qa", "aa")
            self.assertRaises(TypeError)

#test to student -averge -valid
    def test_averge_valid1(self):
        self.student_valid.dic1 = {"qa": 80, "qx": 60, "qs": 55}
        self.assertEqual(self.student_valid.averge(),65)
#test valid id1:id2==
    def test__eq__valid_1(self):
        p1=Student(123,"amit",22)
        p2=Student(123,"aaait",22)
        self.assertTrue((p1==p2))
#false , invalid id1:id2.
    def test__eq__ivalid_1(self):
            p1=Student(113,"amit",22)
            p2=Student(123,"aaait",22)
            self.assertFalse((p1==p2))
#test __gt__ valid
    def test_gt_valid(self):
        p1 = Student(113, "amit", 23)
        p2 = Student(123, "aaait", 22)
        self.assertTrue((p1>p2))
#test __gt__ invalid
    def test_gt_valid(self):
        p1 = Student(113, "amit", 23)
        p2 = Student(123, "aaait", 24)
        self.assertFalse((p1>p2))




