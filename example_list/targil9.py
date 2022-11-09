def group_age (age):
    if age>=0 and age<=18:
        return ("child")
    if age>=10 and age<=60:
        return ("adult")
    if age>=61 and age<=120:
        return ("senior")


for i in range (5):
    age=int(input("enter age:"))
    print(group_age(age))
    