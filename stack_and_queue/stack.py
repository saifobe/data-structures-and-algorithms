from stack_and_queue.node import Node

class Stack:
    """Stack class with push, pop, peek, and is_empty methods"""

    def __init__(self):
        self.top = None

    def push(self, value):
        """Pushes a value to the top of the stack and returns nothing"""

        node = Node(value)

        if self.top == None:
            self.top = node

        else:
            node.next = self.top
            self.top = node

    def pop(self):
        """Removes the top value from the stack and returns it to the user"""

        if self.top == None:
            raise IndexError("This Stack is Empty!!!")
        
        else:
            temp = self.top
            self.top = self.top.next
            return temp.value
        
    def peek(self):
        """Returns the top value from the stack without removing it"""

        if self.top == None:
            raise IndexError("This Stack is Empty!!!")
        
        else:
            return self.top.value
        
   
    
    def is_empty(self):
        """Returns a boolean indicating whether or not the stack is empty"""
        return not bool(self.top)


