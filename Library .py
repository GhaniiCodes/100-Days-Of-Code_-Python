class Library:
    def __init__(self):
        self.Books = []
        
    def Add_Book(self,Books):
        self.Books.extend(Books)
        
    def Info(self):
        print (f"""Number of Books in Library = {len(self.Books)} 
and the Books are :-\n """)
        for index ,i in enumerate(self.Books, start = 1):
            print (f"{index} :  {i} ")
        
    
A = Library()
Books = [ "Pride and Prejudice by Jane Austen",
    "To Kill a Mockingbird by Harper Lee",
    "1984 by George Orwell",
    "Moby-Dick by Herman Melville",
    "The Great Gatsby by F. Scott Fitzgerald","The Road by Cormac McCarthy",
    "Beloved by Toni Morrison",
    "The Goldfinch by Donna Tartt",
    "The Kite Runner by Khaled Hosseini",
    "Life of Pi by Yann Martel","Dune by Frank Herbert",
    "The Hobbit by J.R.R. Tolkien",
    "Neuromancer by William Gibson",
    "Snow Crash by Neal Stephenson",
    "The Name of the Wind by Patrick Rothfuss","The Hunger Games by Suzanne Collins",
    "Harry Potter and the Sorcerer's Stone by J.K. Rowling",
    "The Fault in Our Stars by John Green",
    "Divergent by Veronica Roth",
    "Eleanor & Park by Rainbow Rowell","All the Light We Cannot See by Anthony Doerr",
    "The Book Thief by Markus Zusak",
    "Atonement by Ian McEwan",
    "The Nightingale by Kristin Hannah",
    "The Pillars of the Earth by Ken Follett"]
A.Add_Book (Books)
A.Info()

             
        