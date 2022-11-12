set1={10,22,89,34,66}
set2={22,10,44,32,12}

set3=set1 | set2

print(set3)

set3.pop()
print(set3)

print(max(set3),min(set3))

set4=()
set4=set3.copy()
set4.update({3232,2323})

print(set4)
set4.discard(set1)
set4.discard(set2)
print(set4)