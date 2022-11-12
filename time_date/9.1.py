import time
import datetime

name=input("enter your name:")
age=int(input("enter your age:"))
#השנה בה ימלאו לו 100
time.time()
age_100=(100-age)
x=datetime.datetime.now()+datetime.timedelta(age_100*365)
print(x)

print(x.strftime("%Y"))

date_now=datetime.datetime.now()
print(date_now)
