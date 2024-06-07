import time
t = time.localtime()
#convert the time into formatted string
Time = time.strftime("%Y-%m-%d %H:%M:%S",t)

print(Time)