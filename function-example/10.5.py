def num_found (number, low_number,high_number):
    if number>=low_number and number<=high_number:
        return True
    else:
        return False


num=int (input("enter number:"))
num_low=int (input("enter number low:"))
num_high=int (input("enter number high:"))


if num_found(num,num_low,num_high):
    print("the number is Exists")
else:
    print("not Exists")