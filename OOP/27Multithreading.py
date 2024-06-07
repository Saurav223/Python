import threading
import time

def func(second):
    print(f"Sleeping for {second} seconds")
    time.sleep(second)
    print(f"end{second}")

#func(4)
#func(5)
#func(1)
time1 = time.time()
t1 = threading.Thread(target=func, args=(4,))
t2 = threading.Thread(target=func, args=(2,))
t3 = threading.Thread(target=func, args=(1,))
t1.start()  # .start() method is used to begin the execution of the thread.
t2.start()
t3.start()

#t1.join()  # .join() method is used to wait for a thread to complete its execution.
#t2.join()
#t3.join()
time2 = time.time() - time1
print(f"Time = {time2}")