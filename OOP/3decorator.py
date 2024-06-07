def greet(func):
    def funct(*arg1,**arg2):
        print("Good Morning")
        func(*arg1,**arg2)
        print("Thanks for using this function")
    return funct

@greet
def hello():
    print("Hello World")

@greet
def add(x,y):
    print(f"The sum is {x + y}")

hello()
add(12,34)