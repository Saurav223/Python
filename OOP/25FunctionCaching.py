#just like inline function in c++ which reduce the call return time 
#similarly in python there is function caching for the large program 
#which store chahing of privious computation

from functools import lru_cache
import time

@lru_cache(maxsize=None)  #maxsize is none means it store any size
def funct(n):
    time.sleep(5)
    return n*5


print(funct(5))
print(funct(5))

