world=input("enter world:")
line=input("enter line:")
#רשימה של כל האינדקסים שבהם המילה מופיעה במשפט

count=0
list1=line.split()
for i in list1:
    if world==i:
        count+=1

print(count)





