def average(num1:int,num2:int):
    if type(num1)!=int or type(num2)!=int:
        print("invalid argument . must be int")
        return None
    return (num1+num2)/2



#נשכלל אותו
def valid_grade (grade):
    if type(grade)==str:
        if grade.isnumeric():
            grade==int(grade)
        else:
            return False
    if type(grade)!=int:
        return False

    if 0<=grade<=100:
        return True
    else:
        return False



#קבלה מהיוזר של מספר תקין


def get_grade():
    grade=input("enter number:")

    while not valid_grade(grade):
        grade=input("invalid grade, try again:")

    return grade


grade1 =get_grade()
grade2 =get_grade()

if valid_grade(grade1) and valid_grade(grade2):
    avg=average(grade1,grade2)
    print(avg)

    if avg>=70:
        print("passed")
    else:
         print("failed")
else:
    print("invalid grades")




