
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstring(cls,str):
        return cls(str.split(",")[0],int(str.split(",")[1]))
        #return the class with argument of constructor
e1 = Employee("Saurav", 20000)
print(e1.name)
print(e1.salary)

stringg ="Roman,40000"
e2 = Employee.fromstring(stringg)
print(e2.name)
print(e2.salary)