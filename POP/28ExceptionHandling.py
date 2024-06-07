a = (input("Enter the number: "))
print("The multiplication table is")

try:
    for i in range(1,11):
        print(a,"x",i,"=",int(a)*i)
except:
    print("Error")

print("hELLO WORLD")

try:
    num = int(input("Enter"))
    a = [6,3]
    print(a[num])

except ValueError:
    print("Value isnot integer")

except IndexError:
    print("Index Error")