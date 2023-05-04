from stack_and_queue.node import Node


class Queue:
    """Queue class with enqueue, dequeue, peek, and is_empty methods"""

    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,value):
        """Adds a value to the rear of the queue and returns nothing"""

        node = Node(value)

        if self.front is None:
            self.front = node
            self.rear=node

        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """Removes the front value from the queue and returns it to the user"""


        if self.front is None:
            raise IndexError("This Queue is Empty!!!")
        
        if self.front == self.rear:
            temp = self.front
            self.front = None
            self.rear = None
            return temp.value
        
        else:
            temp = self.front
            self.front = self.front.next
            return temp.value
        
    def peek(self):
        """Returns the front value from the queue without removing it"""

        if self.front is None:
            raise IndexError("This Queue is Empty!!!")
        
        else:
            return self.front.value
        
    def is_empty(self):
        """Returns a boolean indicating whether or not the queue is empty"""
        return not bool(self.front)