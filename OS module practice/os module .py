import os

print("Current Directory : ", os.getcwd())

os.chdir("D:\C ++")   # Changing Directory
print ("Changed Directory : ", os.getcwd())

os.chdir("D:\OS module practice")
print ("Changed Again ",os.getcwd())

print (os.listdir()) # To show files in current Directory 

os.mkdir("OS module 2")


