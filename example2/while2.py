age=int(input("enter age"))

while 0<=age<=120:
    if age >= 0 and age <= 18:
        print("child")
    if age >= 19 and age <= 60:
        print("adult")
    if age >= 61 and age <= 120:
        print("senior")
    age=int(input("enter avilable age"))

print("invaild age")
