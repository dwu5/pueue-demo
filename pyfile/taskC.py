import datetime
from time import sleep

time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time)
sleep(3)
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(time)
sleep(5)
print("C ended")
