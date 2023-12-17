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


    def __str__(self):
        """STR method"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"#
    

    @property
    def width(self):
        """Getter method for Width"""
        return self.__width
    
    
    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    
    @property
    def height(self):
        """Getter method for height"""
        return self.__height
    
    
    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @property
    def x(self):
        """Getter method for x"""
        return self.__x
        
        
    @x.setter
    def x(self, value):
        """Setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    
    @property
    def y(self):
        """Getter method for y"""
        return self.__y
        
        
    @y.setter
    def y(self, value):
        """Setter method for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


    def area(self):
        """calc Area method"""
        return self.__width * self.__height
    

    def display(self):
        """Display method"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(f"{' ' * self.__x}{'#' * self.__width}")
            

    def update(self, *args, **kwargs):
        """Update method"""
        update_args = ["id", "width", "height", "x", "y"]
        for arg, value in zip(update_args,args):
            setattr(self, arg, value)
        
        for key, value in kwargs.items():
            if key in update_args:
                setattr(self, key, value)
           