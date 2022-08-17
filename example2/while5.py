from random import randint
num=randint(9,99)

while 9<num<=99:
    sum = int(num // 10 % 10)
    sum2 = int(num % 10)
    if (num % 7 == 0) or (sum == 7) or (sum2 == 7):
        print(f"lucky number {num} ")
    else:
        print("not lucky)")


    num=int(input("enter number:"))

