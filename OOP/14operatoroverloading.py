# + : __add__
# - : __sub__
# * : __mul__
# / : __truediv__
# < : __lt__
# > : __gt__
# == : __eq__

class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):  # + operator is overloaded by this
        v = Vector(self.i + x.i, self.j + x.j, self.k + x.k)
        return v
    
v1 = Vector(3,4,5)
print(v1)

v2 = Vector(7,8,9)
print(v2)

v3 = v2 + v1
print(v3)

