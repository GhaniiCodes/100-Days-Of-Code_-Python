import os

os.chdir(r"D:\PYTHON\Os Exercise")

jpg_files = [file for file in os.listdir(os.getcwd()) if file.endswith('.jpg')]

jpg_files.sort()
    
for count, file in enumerate(jpg_files, start=1):
    new_name = f"{count}.jpg"
    os.rename(file, new_name)



    