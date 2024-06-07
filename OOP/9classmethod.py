class Employee:
    company = "Google"
    def __init__(self,n):
        self.name = n
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def change(cls,new):
        cls.company = new

e1 = Employee("Saurav")
e1.show()
e1.change("Microsoft")
e1.show()
print(Employee.company)