class Employee:
    name = "Saurav"

e = Employee()
# print(e)  we cannot use obj directly we need to khow the variable name of the class


#str method
class Student:
    def __init__(self,name):
        self.name= name

    def __str__(self):
        return f"The name of the student is {self.name}"


stu = Student("Saurav Subedi")
print(stu)  # Now we can directly return from the name of obj without khowing the name of variable on the class


#call method
class Call:
    def __call__(self):
        print("Hey I am Good")

c = Call()
c()
        
