from random import randint
num=randint(1,9)


num_user=int(input("try to gues the number 1-9:"))

while num>num_user or num<num_user:
    print("try again")
    if num<num_user:
        print("too high")
    else:
        print("too small")



    num_user = int(input("try to gues the number:"))
else:
    print(f" nice guse!: {num}")