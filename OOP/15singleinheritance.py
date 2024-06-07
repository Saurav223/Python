class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def makesound(self):
        print('Sound made by the animal')


class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species ='Dog')
        self.breed = breed

    def makesound(self):
        print("Bark!")

d = Dog('Harry','Golden Ritriver')
d.makesound()

a = Animal('Harry',"Dog")
a.makesound()


        