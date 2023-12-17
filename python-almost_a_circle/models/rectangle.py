"""importing The Base Class From base File"""
from models.base import Base

"""Define the Rectangle class"""
class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates instance object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """Getter method for Width"""
        return self.__width
    
    
    @width.setter
    def width(self, value):
        """Setter method for width"""
        self.__width = value

    
    @property
    def height(self):
        """Getter method for height"""
        return self.__height
    
    
    @height.setter
    def height(self, value):
        """Setter method for height"""
        self.__height = value


    @property
    def x(self):
        """Getter method for x"""
        return self.__x
        
        
    @x.setter
    def x(self, value):
        """Setter method for x"""
        self.__x = value

    
    @property
    def y(self):
        """Getter method for y"""
        return self.__y
        
        
    @y.setter
    def y(self, value):
        """Setter method for y"""
        self.__y = value
