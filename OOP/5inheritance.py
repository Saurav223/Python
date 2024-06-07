class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"THe name of Employee {self.id} is {self.name}")

class Programmer(Employee):
    def __init__(self,lan,name,id):
        super().__init__(name,id)
        self.lan = lan

    def showlanguage(self):
        print(f"The language of this programmer is {self.lan}")


e1 = Employee("Ram",440)
e1.showdetails()

e2= Programmer('C++',40,'Saurav')
e2.showlanguage()