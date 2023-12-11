"""Import the '7-rectangle' File"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Define 'Square' class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size


    def area(self):
        """Define 'area' method"""
        return self.__size * self.__size
