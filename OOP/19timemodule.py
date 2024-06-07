import time
def forloop():
    for i in range(500000):
        i = i + 1
        print(i)

def whileloop():
    i = 0
    while i<500000:
        i = i + 1
        print(i)

T = time.time()  #it return the current time in sec
forloop()
t1 = time.time() - T

whileloop()
t2 = time.time() - T - t1

time.sleep(3)   # it will sleep the python for given second
print("It print after 3 second")

print(f"For Loop : {t1}")
print(f"While Loop : {t2}")

  

