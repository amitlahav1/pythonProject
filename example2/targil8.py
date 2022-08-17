d=int(input("enter day:"))
m=int(input("enter month:"))
y=int(input("enter year:"))

if 1<=d<=31 and 1<=m<=12 and 1950<=y<=2020:
    y1=y%10
    y2=y//10%10
    print(f"{d}/{m}/{y2}{y1}")
else:
    print("failed")





