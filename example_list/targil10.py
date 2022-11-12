def grade_pass (grade):
    grade=int(grade)
    if grade>=70 and grade<=100:
        return True
    else:
        return False



grade=int(input("enter grade:"))

for i in range(4):
    if grade_pass(grade):
        print("paass")
    else:
        print("not pass sorry")
    grade = int(input("enter grade:"))
