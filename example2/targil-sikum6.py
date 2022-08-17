grade=int(input("enter grade: "))
total=0
count=0
total2=0
count2=0

while 0<=grade<=100:
    if grade>=60:
        total += grade
        count += 1
    else:
        total2 += grade
        count2 += 1
    grade = int(input("enter grade: "))
print(f"the averge is: {total/count}")
print(f"the averge faild is: {total2 / count2}")


