"""Define function that check the object 
is exactly an instance of the specified class """#
def is_same_class(obj, a_class):
    return True if isinstance(obj,a_class) else False 
