"""Import '5-base_geometry' File"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a'Rectangle' Class"""
    def __init__(self, width, height):
        """Instantiation width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height


    def area(self):
        """Define 'area' method"""
        return self.__width * self.__height
    

    def __str__(self):
        """'__str__' method to print"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
        