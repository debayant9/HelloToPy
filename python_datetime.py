import datetime
import os

now = datetime.datetime.now()
time = datetime.datetime(2018, 9, 7)
print(time.day)
print(time)
print(now)
time_12 = datetime.datetime.strptime("2018:12:28","%Y:%m:%d")
print(time_12.strftime("%Y"))
print(time_12.day)
time_12.month
ls = os.listdir()
print(ls[2])
