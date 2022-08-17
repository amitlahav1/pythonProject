grade=int(input("enter valid grade:"))
invalid=0

while 0<grade<=100:
    invalid+=1
    if invalid==5:
        print ("to many valid grades")
        break
    grade = int(input("enter valid grade:"))

else:
    print ("invalid grade")

