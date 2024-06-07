def func():
    try:
        lis = [1,2,3,4,5,6]
        index = int(input("Enter the index"))
        print(lis[index])
        return 1
    except:
        print("Some error")
        return 0
    finally:
        print("I am always awesome")
    
x=func()
print(x)

    
    
