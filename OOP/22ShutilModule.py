import shutil 
shutil.copy("main.py","main2.py")
shutil.copytree(".tutorial","mytutorial")
shutil.move(".tutorial/file.file","file.file")
shutil.rmtree("mytutorial")