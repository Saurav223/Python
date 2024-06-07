# print(a = False) throw error
print(a:=False)  # walrus operator



choice = ""
while True:
    choice = input("You wanna continue Y/N ")
    if choice == "n" or choice == "N":
        break
    print("Hello")


print("Thats aam jindagi")

choices = ""
while(choices := input("Do you wanna continue Y/N ")) != "n":
    print("Hello")

print("Thats mentos jindagi")
