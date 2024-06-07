f =open('marks.txt','r')
i = 0
while True:
    i = i +1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of Student {i} in Maths is:{m1*2}")
    print(f"Marks of Student {i} in Science is:{m2}")
    print(f"Marks of Student {i} in English is:{m3}")
f.close()