"""importing The Rectangle Class From rectangle File"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Creates instance object"""
        super().__init__(size, size, x, y, id)
    

    def __str__(self):
        """Overriding STR method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"    


    @property
    def size(self):
        """Getter method for size"""
        return self.__size
    

    @size.setter
    def size(self, value):
        """Setter method for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value
    