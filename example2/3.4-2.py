from random import randint
num_system=randint(0,100)
count=0
print(f" the number of system is: {num_system}")
num_user=int(input(" think number 1-100:"))

while num_system!=num_user:
    count+=1
    user=input("write if the number of the system is- high or low?:")
    if user=="low":
        num_system = randint(num_user, 100)
    if user=="high":
        num_system = randint(0, num_system+1)

    print(f" the number of system is: {num_system}")

else:
    print(f"after {count} you gues ")



