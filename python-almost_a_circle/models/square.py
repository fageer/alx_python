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
