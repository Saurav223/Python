class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def showdetails(self):
         print(f"Name : {self.name}")
         print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name,"Dog")
        self.breed = breed

    def showdetails(self):
        super().showdetails()
        print(f"Breed: {self.breed}")

class GoldenRetriver(Dog):
    def __init__(self,name,age):
        super().__init__(name,"Golden Retriver")
        self.age = age

    def showdetails(self):
        super().showdetails()
        print(f"Age : {self.age}")

micky = GoldenRetriver("Micky","5 yrs")
micky.showdetails()
    
    


    



