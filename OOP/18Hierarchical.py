class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Name = {self.name}")
        print(f"Id = {self.id}")

class Manager(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary

    def show(self):
        super().show()
        print(f"Salary = {self.salary}")

class CEO(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary

    def show(self):
        super().show()
        print(f"Salary = {self.salary}")

ram = Manager("Ram",20,200000)
ram.show()

hari = CEO("Hari",25,250000)
hari.show()
