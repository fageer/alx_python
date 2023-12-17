"""importing The Base Class From base File"""
from base import Base

"""Define the Rectangle class"""
class Rectangle(Base):
    """Define The __init__ method"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inherit the init method from the super class"""
        super().__init__(self, id)
        """Assign each argument """
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """Getter method for width"""
        return self.width
    
    
    @width.setattr
    def width(self, value):
        """Setter method for width"""
        self.width = value

    
    @property
    def height(self):
        """Getter method for height"""
        return self.height
    
    
    @height.setattr
    def height(self, value):
        """Setter method for height"""
        self.height = value


    @property
    def x(self):
        """Getter method for x"""
        return self.x
        
        
    @x.setattr
    def x(self, value):
        """Setter method for x"""
        self.x = value

    
    @property
    def y(self):
        """Getter method for y"""
        return self.y
        
        
    @y.setattr
    def y(self, value):
        """Setter method for y"""
        self.y = value
