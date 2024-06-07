def cube(x):
    return x * x * x

l = [2,3,4,5,6,7,8]

#newl = []
#for i in l:
#    newl.append(cube(i))

newl = list(map(cube,l))
print(newl)

def filters(a):
    return a>4


newnewl = list(filter(filters,l))
print(newnewl)

#map with direct lambda function
newl2 = list(map(lambda x: x * x,l))
print(newl2)

