num=int(input("choose number 0-100:"))
from random import randint
num_system=randint(0,100)
count=0

while num>num_system or num<num_system:
    count+=1
    if num_system>num:
        print("sorry system but - the number high ")
    else:
        print(" sorry system but - the number small")
    num_system = randint(0, 100)

    num = int(input("put again the number, let another try to system :"))


else:
    print(f" nice gues. the number of try was:{count}")
















