from stack_and_queue.Animal import Animal,Cat,Dog
from stack_and_queue.node import Node
from stack_and_queue.queue import Queue

class AnimalShelter:
    """a class called AnimalShelter which holds only dogs and cats and uses separate Queue for each animal
    
    Attributes:

    dogs (Queue): A queue of dogs in the shelter.
    cats (Queue): A queue of cats in the shelter.
    """
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal:Animal):
        """Adds an animal (either a dog or a cat) to the queue"""
        if animal.species == "dog":
            self.dogs.enqueue(animal)

        if animal.species == "cat":
            self.cats.enqueue(animal)

    def dequeue(self, pref):
        """Removes and returns the next available animal of the specified"""

        if pref == "dog" and not self.dogs.is_empty():
           return self.dogs.dequeue() 

        if pref == "cat" and not self.cats.is_empty():
           return self.cats.dequeue() 

        if pref != "dog" or pref != "cat":
            return None

      
if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue(Cat("Fluffy"))
    shelter.enqueue(Dog("Spot"))
    shelter.enqueue(Cat("Whiskers"))
    shelter.enqueue(Cat("Patches"))
    shelter.enqueue(Dog("Rover"))
    shelter.enqueue(Dog("Fido"))
    print(shelter.dequeue("dog").name)  # Spot
    print(shelter.dequeue("dog").name)  # Rover
    print(shelter.dequeue("cat").name)  # Fluffy
    print(shelter.dequeue("cat").name)  # Whiskers
    print(shelter.dequeue("cat").name)  # Patches
    print(shelter.dequeue("cat"))  # None
    print(shelter.dequeue("dog").name)  # Fido
    print(shelter.dequeue("dog"))  # N
    
        
 
