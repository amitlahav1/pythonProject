world=input("enter world:")
line=input("enter line:")
#רשימה של כל האינדקסים שבהם המילה מופיעה במשפט


list_index=[]
start_intex=0

for i in range(line.count(world)):
    found_index=line.index(world, start_intex)
    list_index.append(found_index)
    start_intex=found_index+1


print(list_index)


