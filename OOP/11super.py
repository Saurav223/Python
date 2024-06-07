class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def Print(self):
        print(f"The name of the employee is {self.name} and id is {self.id}")

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang = lang
    
    def Print(self):
        super().Print()
        print(f"The language of the programmer is {self.lang}")

emp1 = Programmer('Saurav',440,'C++')
emp1.Print()    

