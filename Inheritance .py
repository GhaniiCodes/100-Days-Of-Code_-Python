class Employee:
    def __init__(self):
        self.name = input("Enter name of employee: ")
        self.ID = input("Enter Employee ID: ")

    def info(self):
        print(f"Employee Name = {self.name} and  ID = {self.ID}")


class Mananger(Employee):
    def __init__(self):
        super().__init__()
        self.Title = input("Enter Title (MR or MRs) : ")
        self.Expenses = input("Enter Expenses : ")
        
    def info(self):
        print (f"{self.Title} {self.name} having ID = {self.ID} and having Expenses = {self.Expenses}")
        



A = Employee()
A.info()
B = Mananger()
B.info()