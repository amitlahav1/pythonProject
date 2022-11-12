def valid_num (num1):
    if num1<=999 and num1>=100:
        return True
    else:
        return False

num_user=int(input("enter number with 3 digits:"))



if valid_num(num_user):
    print("the number with 3 digits")
else:
    print("not valid")


