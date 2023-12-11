"""Import '5-base_geometry' File"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a'Rectangle' Class"""
    def __init__(self, width, height):
        """Instantiation width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
