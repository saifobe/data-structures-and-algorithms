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


    

