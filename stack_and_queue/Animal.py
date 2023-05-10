class Animal:
    """super class for Dog and Cat 
    
        Arguments: name,species"""
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Dog(Animal):
    """Sub class for Animal that takes Animal class Arguments
    
        Arguments: name, species="dog" """
    def __init__(self, name):
        super().__init__(name, species="dog")

class Cat(Animal):
    """Sub class for Animal that takes Animal class Arguments
    
        Arguments: name, species="cat" """
    def __init__(self, name):
        super().__init__(name, species="cat")

