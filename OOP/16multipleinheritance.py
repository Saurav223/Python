class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

class Programmer(Employee,Teacher):
    def __init__(self,name,id,subject,language):
        Employee.__init__(self,name,id)
        Teacher.__init__(self,name,subject)
        self.language = language

    def show(self):
        print(f"The name of the Employee of id {self.id} is {self.name} and teaches the {self.subject} subject and program in {self.language} ")

pro = Programmer("Saurav", 40, 'OOP' , 'C++')
pro.show()




