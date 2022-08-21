
list1=[]
num=int(input("enter number :"))

for i in range(5):
    list1.append(num)
    num = int(input("enter number "))

print(*list1)
print(f" this the max number {max(list1)}")
print(f"this min number: {min(list1)}")
print(f"this average: {sum(list1)/len(list1)}")
