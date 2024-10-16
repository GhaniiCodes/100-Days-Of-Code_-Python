import random

Play_Again = int(input("Press 1 to Continue : "))
while (Play_Again == 1):
    
    
    Choices = ["Water","Gun","Snake"]
    Random = random.choice(Choices)
    
    User_Choice = input("Enter Your Choice ").capitalize()
    print ("User Choice : ",User_Choice)
    print ("Computers Choice : ", Random)
    
    if (User_Choice == Random):
        print ("Its a Draw")
    
    elif (User_Choice == "Water" and Random == "Snake"):
        print ('''Snake Has Poisened The Water
        And computer Wins''')
        
    elif (User_Choice == "Water" and Random == "Gun"):
        print ('''Water has Rusted the Gun
        And the user Wins''')
        
        
    elif (User_Choice == "Gun" and Random == "Water"):
        print ('''Gun is Rusted by Water
        And the Computer Wins''')
        
    elif (User_Choice == "Gun" and Random == "Snake"):
        print ('''Snake is Shot by Gun 
        And the User Wins''')    
    
    
    
    elif (User_Choice == "Snake" and Random == "Water"):
        print ('''Snake Poisoned The Water 
        and the User Wins''')
    
    
    elif (User_Choice == "Snake" and Random == "Gun"):
        print ('''Snake is Shot by Gun
        and the Computer Wins''')
        
    else:
        print ("Invalid Input")
    
    Play_Again = int(input('''If you want to play Again Enter One ( 1 )
    Otherwise Press Any key ''')) 


