"""Define Base Class"""
class Base:
    """private class attribute """
    __nb_objects = 0
    """class constructor"""
    def __init__(self, id=None):
        """Check if the id is none"""
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
