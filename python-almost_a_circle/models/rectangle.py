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
