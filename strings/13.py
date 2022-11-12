signal=input("enter signal:")
line=input("enter line:")


for i in range(len(line)):
    if (signal==line[i]):
        line=line[:i]+line[i].capitalize()+line[i+1]

print(line)