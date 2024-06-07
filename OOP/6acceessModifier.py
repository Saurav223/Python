class Employee:
    def __init__(self):
        self.name1 = "Saurav"   #public
        self.__name2 = "Saurav Subedi" #private
        self
a = Employee()
print(a.name1)
# print(a.name2)
#Cannot be accessed directly

print(a._Employee__name2) #Can be accessed directly