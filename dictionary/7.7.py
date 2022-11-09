dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 4, 6: 60,7:10,}
#להסיר ערכים כפולים

dic2={}
for key in dic1:
    if dic1[key] not in dic2.values():
        dic2.update({key:dic1[key]})



print(dic2)