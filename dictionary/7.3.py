dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 4, 6: 60}

dic2={}

for i in dic1:
    dic2[dic1[i]]=i

print(dic2)