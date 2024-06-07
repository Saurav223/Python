s1 = {1,2,3,5}
s2 = {3,5,6,7}


print(s1.union(s2))
print(s1,s2)

s1.intersection_update(s2)
print(s1)

s3 = s1.symmetric_difference(s2) #all element except common element
print(s3)

s4 = {4,5,6,7,8,9}
print(s4.difference(s2))

print(s2.isdisjoint(s4)) #no common element

print(s1.issuperset(s2))  # if s2 contains all the elemts of s1 then it is superset
print(s1.issubset(s2))  # if s1 contain all the elemenmt of the s2

name1 = {'ram','hari','krishna'}
name1.add('shiva')    # it will add only one items
print(name1)

name1.discard('hari') #we can use "remove" instead of "discard" if the element isnot find remove throw an error
print(name1)

