import time
import datetime

date_now=datetime.datetime.now()
d=(date_now.strftime("%d"))
m=(date_now.strftime("%m"))
y=(date_now.strftime("%y"))

print(f"{d}/{m}/{y}")
print(f"{m}/{d}/{y}")

print(d)
print(y)
print(m)