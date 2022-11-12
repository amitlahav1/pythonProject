num=int(input("deposit amount : "))
num2=int(input("deposit amount evrey month : "))
num3=int(input("interest of year % : "))
num4=int(input("number of year : "))

sum=float(num4*12*num2+num)
sum2=float(num3/100)
sum4=float(sum2*sum+sum)
sum3=float(sum4+sum)

print(f"the deposit amount is : {sum}")
print(f"the profit is : {sum4}")
print(f"the all amount is : {sum3}")




print("--------- ter2 for github")
