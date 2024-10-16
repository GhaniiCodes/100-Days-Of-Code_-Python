class Student:
    Depeartment = "Artificial Intelligence"
    
    @classmethod
    def Change_Department(self):
        self.Depeartment = "Computer Science"
    
    def Info(self):
        print (f"{self.Name} is in {self.Depeartment} Department ")
    
  
        
        
A = Student()
A.Name = "Muhammad"
A.Info()

B = Student()
B.Name = "Usman"
B.Change_Department()
B.Info()

C = Student()
print (C.Depeartment)