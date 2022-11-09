import datetime
import time

time.time()
print(time.time())
print(time.strftime("%A"))
print(time.strftime("%d"))
print(time.strftime("%D"))
print(time.strftime("%M"))
print(time.localtime())
print(time.asctime())
print("print(time.asctime())")
print(datetime.datetime.now())
print(datetime.datetime(2022,12,31 , 23,59,59)-datetime.datetime.today())
print(datetime.datetime.now()+datetime.timedelta(days=10))
x=datetime.datetime.now()+datetime.timedelta(days=10)
print(x.time())
print(x.date())
x=datetime.datetime.now()+datetime.timedelta(days=1)
print(x.strftime("%A"))




