from linked_list.node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return self.to_string()
    
    def append(self,value):
        """Adds a new node with that value to the end of the list 
        Args:
            value: value of the new node
            
            Returns: nothing
            
            Raises: nothing"""

        node = Node(value)
        
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def insert(self, data):
        """Inserts a new node with that value before the first node of the list
        Args:
            value: value of the new node
            
            Returns: nothing
            
            Raises: nothing """
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def includes(self,data):
        """Indicates whether that value exists as a Node’s value somewhere within the list.
        Args:
            value: value of the new node
            
            Returns: Boolean
            
            Raises: nothing """
        current = self.head
        while current is not None:
            if current.value == data:
                return True
            current = current.next
        return False

    def to_string(self):
        """Returns: a string representing all the values in the Linked List, formatted as:
        "{ a } -> { b } -> { c } -> NULL"
        Args:
            value: value of the new node
            
            Returns: string
            
            Raises: nothing """
        current_node = self.head
        result = ""
        while current_node:
            result += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next
        result += "NULL"
        return result


    

