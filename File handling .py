## Reading A File 

with open ('File Handling.txt', 'r') as A:
    print (A.read())


## Writting in a File 

with open ('File Handling 2.txt', 'w') as B:
    B.write("This is how to write BRO ")

## Appending in File 

with open ('File Handling.txt', 'a') as A:
    A.write("\n\n And congratulation we know how to append now**")
    

with open ('File Handling.txt', 'r') as A:
    print (A.read())
    
    
## Creating a File 

open ("File Handling  3.txt", 'x')
    
    
    