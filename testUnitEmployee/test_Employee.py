from unittest import TestCase
from Employee import Employee

class TestEmployee(TestCase):

    def setUp(self):
        self.emp = Employee('amit', 'lahav', 100)


    def test_email(self):
        self.assertEqual("amit.lahav@email.com", self.emp.email())




    def test_fullname(self):
        self.assertEqual('amit lahav',self.emp.fullname())

    def test_apply_raise(self):
        self.emp.apply_raise()
        self.assertEqual(self.emp.pay,105)


