class Person:
    def __init__(self, name, age, number_Children):
        self.name=name
        self.age=age
        self.number_kids=number_Children

    def hasChildren(self, number_Children):
        if number_Children>0:
            return True
        else:
            return False

    def ageGroup(self, age):
        if age>=0 and age<=18:
            return ("Chiled")
        if age>=19 and age<=60:
            return ("Adult")
        if age>=61 and age<=120:
            return ("Senior")

    def __str__(self):
        return (f"the name is:{self.name}, the age is:{self.age}, the number of children is:{self.number_kids}")


name=input("enter your name:")
age=int(input("enter please your age:"))
children=int(input("how many children do you have?"))
person1=Person(name,age,children)
print(person1)

if person1.hasChildren(children):
    print("have children")
else:
    print("not have children")

print(person1.ageGroup(age),"this the group")