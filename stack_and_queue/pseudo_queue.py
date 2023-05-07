from stack_and_queue.node import Node
from stack_and_queue.stack import Stack



class PsuedoQueue:

    def __init__(self):
        """declare two stacks as instance variables """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        """pushes a value to the top of stack1"""

        self.stack1.push(value)

    def dequeue(self):
        """removes the front value from the queue and returns it to the user"""
        if self.stack2.is_empty():# if stack2 is empty, pop all elements from stack1 and push them to stack2
            while not self.stack1.is_empty(): # while stack1 is not empty
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()
    
if __name__ == "__main__":
        q = PsuedoQueue()
        q.enqueue(10)
        q.enqueue(15)
        q.enqueue(20)
        print(q.dequeue())  # prints 10
        