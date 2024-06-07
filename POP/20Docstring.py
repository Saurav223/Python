#doc string is a string which is writen just after the 
# function or class defination and unlike comment it can asscessible
def square(n):
    '''It takes a numnber and return square of it'''
    print(n**2)

square(5)
print(square.__doc__)  #this line is used to asscess the doc string
    