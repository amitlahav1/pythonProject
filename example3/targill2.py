pas=input("enter password:")
pas_va=input("enter password again:")

for i in range (5):
    if pas!=pas_va:
        pas_va = input("enter password again:")
else:
    print("finish")



