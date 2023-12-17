"""importing The Base Class From base File"""
from base import Base

"""Define the Rectangle class"""
class Rectangle(Base):
    """Define The __init__ method"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inherit the init method from the super class"""
        super().__init__(self, id)
        """Assign each argument """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y


    @property
    def width(self):
        """Getter method for width"""
        return self.__width
    
    
    @width.setattr
    def width(self, value):
        """Setter method for width"""
        self.__width = value

    
    @property
    def height(self):
        """Getter method for height"""
        return self.__height
    
    
    @height.setattr
    def height(self, value):
        """Setter method for height"""
        self.__height = value


    @property
    def x(self):
        """Getter method for x"""
        return self.__x
        
        
    @x.setattr
    def height(self, value):
        """Setter method for x"""
        self.__x = value
