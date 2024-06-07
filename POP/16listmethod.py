lst = [11,2,3,4,5,6,3,8,9]
print(lst)

lst.append(10)
print(lst)

lst.sort() #ascending order
print(lst)

lst.reverse() #desending order
print(lst)

print(lst.index(6))  #it return the index of the given element

print(lst.count(3))  # it return  the count of the given eleemts

m = [900,33,5342,25]
lst.extend(m) #it merge the the list
print(lst)

k = lst + m #it merge the two list and put in another list
print(k)
