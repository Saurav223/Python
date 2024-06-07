import os

if(not os.path.exists("DATA")):  #create DATA folder if not exist
   os.mkdir("DATA")


# for i in range(0,3):   
   # os.mkdir(f"DATA/Hello{i+1}")    #create HEllO file in DATA folder
 #  os.rename(f"DATA/HELLO{i+1}",f"DATA/BYE{1+i}")   rename this into BYE

folders = os.listdir("DATA")  #checking the no. of folder in the DATA folder

for fol in folders:
   print(fol)
   print(os.listdir(f"DATA/{fol}"))  #print the content of the individual folder

print(os.getcwd)    #get the current directory
