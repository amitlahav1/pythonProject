
# world=(input("enter world:"))
#
# for i in world:
#     if i=='a' or i=='A':
#         continue
#     else:
#         print(i,end="")


string=input("world:")
string=string.replace('a',"")
string=string.replace('A', "")
print(string)