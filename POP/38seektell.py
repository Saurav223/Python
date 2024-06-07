with open('myfile.txt','r') as f:
    f.seek(10)     # it just move the cursor from the given position
    print(f.tell())  # it tell the position of cursor of the file
    text = f.read()
    print(text)