class Student:
   def __init__(self,n,o):   #constructor
      self.name = n
      self.faculty = o

   def info(self):
      print(f"The name is {self.name} and faculty is {self.faculty}") 

a = Student("Saurav","BEI")
b = Student("Hari","BCT")

a.info()
b.info()