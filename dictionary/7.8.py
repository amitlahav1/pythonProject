list_name=["amit","tal", "yosi", "idan", "dan"] #this ky
list_grade=[100,90,60,77,80]

sum=sum(list_grade)
averge=sum/5
print(averge, ", this the averge")
dic1={}

for key in list_name:
    for value in list_grade:
        dic1[key] = value
        list_grade.remove(value)
        break

print(dic1)
list_top=[]
for i in dic1:
    if dic1[i]>averge:

     print(i)
