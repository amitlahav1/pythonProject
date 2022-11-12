
def sum_digits (num1):
    num2=num1//100
    num3=num1//10%10
    num4=num1%10
    return (num3+num2+num4)

num_user=int(input("enter number with 3 digits:"))
print(sum_digits(num_user))
