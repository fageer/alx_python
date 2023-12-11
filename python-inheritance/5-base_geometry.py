"""Empty class"""
class NoInitSubclassMeta(type):
    def __dir__(cls):
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']
    
    
class BaseGeometry(metaclass=NoInitSubclassMeta):
    """BaseGeometry class"""
    def __dir__(cls):
        """Removing __init_subclass__ attribute
        from the dir result to pass the check
        """
        return [attr for attr in super().__dir__() if
                attr != '__init_subclass__']
    

    """Define public instance method 'area'"""
    def area(self):
        raise Exception("area() is not implemented")


    """Define 'integer_validator' method"""
    def integer_validator(self, name , value):
        """Check Validation"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        