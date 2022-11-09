#בניית פונקציה לחישוב ממוצע . תקבל 2 מספרים ותחשב את הממצוע
#אם הממוצע גדול או שווה ל70 אז יעבור אם לא "ייכשל"
def average(num1,num2):
    avg=(num1+num2)/2
    return avg
#נכין עוד פונקציה שתקבל מספר ותחזיר תשובה אם ציון תקין

def valid_grade (grade):
    if 0<=grade<=100:
        return True
    else:
        return False



#עד לכאן כתבנו את הפונקציה - מעכשיו נתחיל לכתוב את הקוד שלנו
grade1=int(input("enter grade:"))
grade2=int(input("enter grade 2:"))

if valid_grade(grade1) and valid_grade(grade2):
    average(grade1,grade2)
    print(average(grade1,grade2))

    if average(grade1,grade2)>=70:
        print("passed")
    else:
         print("failed")
else:
    print("invalid grades")

