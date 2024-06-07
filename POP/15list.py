marks = [3,4,5,'Saurav',True,3,54,5,67,37]
print(marks)
print(type(marks))
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[len(marks)-3])
print(marks[1:3])  #print between that index
print(marks[1:8:2]) #it print between the index with jumming with index

 # in keyword is used in list to search any element
if "Saurav" in marks:
    print('Yes')
if 4 in marks:
    print('Yes')

# list conprehension 
lst = [i+1 for i in range(50) if i % 2 == 0]
print (lst)