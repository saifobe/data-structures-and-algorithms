# data-structures-and-algorithms


# Challenge Title
Linked List

## Whiteboard Process
    None

## Approach & Efficiency
Create a Linked List class that includes
- A method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- A method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.

## Solution

``` python
from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return self.to_string()
    
    def append(self,value):

        node = Node(value)
        
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def includes(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def to_string(self):
        result = ""
        current = self.head
        while current is not None:
            result += f"{current.data} -> "
            current = current.next
        result += "NULL"
        return result

```

### Saif Obeidat