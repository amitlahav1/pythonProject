import time
import datetime
time.time()
from time import strptime



y_born=input("enter your year of you born:, format=2014 :")
d_born=input("enter your day of you born:, format=2,20,4 :")
m_born=input("enter your month of you born:, format=Jan,feb :")

y=y_born[0:4]
print(y)
d=d_born[0:2]
print(d)
m=m_born[0:3]
print(m)

d=int(d)
if d<10:
    list=d
print(d)

month_num = datetime.datetime.strptime('m', '%b').month
print(month_num)

date={y},{month_num},{d}
print(date)

