"""Define an Empty Class"""
class BaseGeometry:
    """it's an empty class"""
    def __dir__(self):
        if hasattr(self, '__dict__'):
            return [attr for attr in dir(type(self)) if attr != '__init_subclass__']
        else:
            return dir(type(self))
