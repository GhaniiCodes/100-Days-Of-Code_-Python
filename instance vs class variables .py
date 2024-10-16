class student:
    University_Name = "Islamia University Peshawar"    #Class Variable
    def __init__(self): 
        self.Name = "Muhammad" 
        self.Roll_Number = 232502
        self.Department = "Artificial Intelligence"
        self.GPA = 4.00
        
        
    def info(self):
        print (f"""\n\n "{self.Name}" having Roll Number "{self.Roll_Number}"
    is in "{self.Department}" Department at "{self.University_Name}"
    has got "{self.GPA}" GPA""")
        

A = student()
A.University_Name = "Peshawar University"
A.info()
B = student()
B.Name = "Usman"
B.Roll_Number = 232501
B.Department = "Artificial Intelligence"
B.GPA = 3.90
B.info()
C = student()
C.Name = "Ghani"
C.Department = "Artificial Intelligence"
C.Roll_Number = 232503
C.GPA = 3.98
C.info()