emp = {40:33,41:56,42:78,43:89}
emp2 = {44:56,45:90}

emp.update(emp2)
print(emp)

#emp.pop(40)
emp.popitem() #pop the last item
print(emp)

emp.clear()
print(emp)