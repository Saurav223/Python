def average(a,b):
    print('THe average is',(a+b)/2)

#default
def av(a,b=3):
    print("hello")
   
average(4,6)
av(3)

#return
def multiply(x,y):
    mul = x * y
    return mul

c = multiply(20,4)
print(c)