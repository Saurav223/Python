import os 

def rename(direc):
    files = os.listdir(direc)
    jpgfile = []

    for file in files:
        if file.endswith('.jpg'):
            jpgfile.append(file)

    for i in range(1,len(jpgfile) + 1):
        oldfile = os.path.join(direc,jpgfile[i-1])
        newfile = os.path.join(direc,f'{i}.jpg')
        os.rename(oldfile,newfile)
print(os.getcwd())
rename(os.getcwd())
