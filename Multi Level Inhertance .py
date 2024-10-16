class Employee:
    def __init__(self):
        self.Name = input("Enter Name: ")
        self.ID = input("Enter ID: ")
        
    def show_details(self):
        print(f"""Employee Information:
Employee: {self.Name}
ID: {self.ID}""")
        
class Intern(Employee):
    def __init__(self):
        super().__init__()   
        self.Salary = int(input("Enter Salary: "))
        
    def show_details(self):
        super().show_details()
        print(f"Salary: {self.Salary}")

class Manager(Intern):
    def __init__(self):
        super().__init__()
        self.Travel_Expense = int(input("Enter Travel Expence : "))
    
    def show_details(self):
        super().show_details()
        print(f"Travel Expense : {self.Travel_Expense}")
        
class CEO(Manager):
    def __init__(self):
        super().__init__()
        self.Night_Stay_Expense = int(input("Enter Night Stay Expense : "))
        self.Food_Expense = int(input("Enter Food Expense : "))
        self.Meeting = input("Next Meeting with Client is On : ")
        
    def show_details(self):
        super().show_details()
        print (f"""Night Stay Expense : {self.Night_Stay_Expense}
Food Expense : {self.Food_Expense}
Next Meeting Is on : {self.Meeting}""")
        
        
A = CEO()
A.show_details()             