f = open('myfile.txt','r')

text = f.read()
print(text)
f.close()

g = open('myfile.txt','a')
g.write("HEllo Wrold")
g.close()

#short cut on need to close
with open('myfile.txt','a') as f:
    f.write("Hey I am ")
