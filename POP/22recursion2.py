
def fib(n):
    if(n==0 or n==1):
        return n
    
    else:
        return fib(n-1) + fib(n-2)

num = int(input("Enter the range of fibonaci series: "))
for i in range(num):
    print(fib(i))
