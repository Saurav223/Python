#when two same value immutable object is created
#python store it in same memory loction so they are exactly same "is return true"

a = 3  #constant
b = 3  #constant

print(a is b) #exact location of object in memory
print(a == b) # value

c = [1,2,33]  #not cons
d = [1,2,33]
print(c is d)
print(c == d)
