class Person:
    name = 'Saurav SUbedi'
    occupation = 'Student'
    subject = 'BEI'
    year = '2nd'
    def info(self):
        print(self.name)

a = Person()
print(a.name)
a.info()

b = Person()
b.name = "Sauravvv"
b.info()