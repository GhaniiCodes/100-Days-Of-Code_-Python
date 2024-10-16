class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def Area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, Radius):
        self.Radius = Radius
        
    def Area(self):
        return 3.14 * (self.Radius * self.Radius)
    
class Square(Shape):
    def __init__(self, Side):
        self.Side = Side
        
    def Area(self):
        return self.Side * self.Side 
    

Rec = Shape(10,15)
print (Rec.Area())

Cir = Circle(3)
print (Cir.Area())

Sq = Square(5)
print (Sq.Area())
    
         