class Fruit:
    def __init__(self,name):
        self.name = name
    
    @property
    def fruit_name(self):
        print(f'{self.name} was accessed')
        return self.name

    @fruit_name.setter
    def fruit_name(self,name):
        print(f"{self.name} is now {name}")
        self.name = name

    @fruit_name.deleter
    def fruit_name(self):
        print(f'{self.name} was deleted')
        del self.name

fruit = Fruit('Banana')
print(fruit.fruit_name)   # Parenthesis is not used in getter setter and deleter

fruit.fruit_name = "Orange"
print(fruit.fruit_name)

del fruit.fruit_name
print(fruit.fruit_name)














