class Employee: 
    companyName = 'Microsoft'  #class variable
    def __init__(self,name):
        self.name = name
        self.raisee = 0.2

    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in company {self.companyName} is {self.raisee}")

emp1 = Employee('Saurav')
emp1.raisee = 0.3  #instance variable
emp1.showDetails()

emp2 = Employee('Ram')
#When a class Variable is change it create a new instance varible
#which is accosicate with object but the class variable isnot change
emp2.companyName = "Google"
emp2.showDetails()

print(Employee.companyName)  #It is not by using the object
