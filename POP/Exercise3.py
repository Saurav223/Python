import random
import string


def coding(a):
    c = ""
    b = len(a)
    if(b < 3):
        for i in a:
            c = i + c
    else:
        tmp = a[0]
        a = a + tmp
        for i in range(1,b+1):
            c = c + a[i]
        c = randomm() + c + randomm()
    return c    

def randomm():
    letter = ''.join(random.choices(string.ascii_letters,k=3))
    return letter

def decoding(a):
    b = len(a)
    c =""
    if(b<3):
        for i in a:
            c = i + c
        
    else:
        tmp=''
        for i in range(3,b-3):
            tmp = tmp + a[i]
        c = tmp[len(tmp)-1]
        for i in range(0,len(tmp)-1):
            c = c + tmp[i]
    return c

message = 'Kathmandu'
secret = coding(message)
print(secret)
print(decoding(secret))
    
        




