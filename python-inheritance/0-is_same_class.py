"""Define 'is same class' Function"""
def is_same_class(obj, a_class):
    """Check The Object is Exactly an instance of the Specified Class """
    return True if isinstance(obj,a_class) else False 
