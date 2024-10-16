with open ("Students Marks .txt",'w') as M:
    M.write("""John : 85
Emily : 92
Michael : 78
Sarah : 88
David : 76
Jessica : 90
James : 82
Emma : 85
Jacob : 79
Olivia : 91
Matthew : 84
Sophia : 89
Ethan : 77
Isabella : 93
William : 80
Ava : 87
Alexander : 83
Mia : 94
Benjamin : 81
Harper : 86""")


with open ("Students Marks .txt",'r') as M:
    print (M.read())
    
    Marks = {}
    for line in M:
        Name , Mark = line.split(":")
        Marks[Name] = int(Mark)
        

print (Marks)
