# data-structures-and-algorithms


# Challenge Title
Linked List

## Whiteboard Process
    
![code Challenge 06](Untitled%20(3).jpg  "Linked List")

## Approach & Efficiency
Create a Linked List class that includes
- A method called insert which takes any value as an argument and adds a new node with that value to the head of the list with an O(1) Time performance.
- A method called includes which takes any value as an argument and returns a boolean result depending on whether that value exists as a Node’s value somewhere within the list.
- A method called toString which takes in no arguments and returns a string representing all the values in the Linked List, formatted as:
"{ a } -> { b } -> { c } -> NULL"
- A method called append which adds a new node with the given value to the end of the list, with an O(1) Time performance.
- A method called insertBefore which adds a new node with the given newValue immediately before the first value node, with an O(1) Time performance.
- A method called insertAfter which adds a new node with the given newValue immediately after the first value node, with an O(1) Time performance.

## Solution

``` python
from linked_list.node import Node

class LinkedList:

    """
    A class representing a linked list, a data structure made up of a sequence of nodes, each containing some data
    and a reference to the next node in the sequence.

    Attributes:
    ----------
    head : Node or None
        The first node in the linked list, or None if the list is empty.
    """
    
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Inserts a new node containing the given value at the beginning of the linked list.

        Parameters:
        ----------
        value : any
            The value to be stored in the new node.

        Returns:
        -------
        None
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        """
        Adds a new node containing the given value at the end of the linked list.

        Parameters:
        ----------
        value : any
            The value to be stored in the new node.

        Returns:
        -------
        None
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_before(self, value, new_value):
        """
        Inserts a new node containing the given new_value before the first occurrence of the given value in the linked list.

        Parameters:
        ----------
        value : any
            The value to search for in the linked list.
        new_value : any
            The value to be stored in the new node.

        Returns:
        -------
        None
        """
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def insert_after(self, value, new_value):
        """
        Inserts a new node containing the given new_value after the first occurrence of the given value in the linked list.

        Parameters:
        ----------
        value : any
            The value to search for in the linked list.
        new_value : any
            The value to be stored in the new node.

        Returns:
        -------
        None
        """
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node:
            if current_node.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def includes(self, value):
        """
        Inserts a new node containing the given new_value after the first occurrence of the given value in the linked list.

        Parameters:
        ----------
        value : any
            The value to search for in the linked list.
        new_value : any
            The value to be stored in the new node.

        Returns:
        -------
        None
        """
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def to_string(self):
        """
        Returns a string representation of the linked list, with each node's value enclosed in curly braces and
        separated by arrow symbols pointing to the next node. The last arrow points to NULL to indicate the end of the
        list.

        Returns:
        -------
        str
            A string representation of the linked list.
        """
        current_node = self.head
        result = ""
        while current_node:
            result += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next
        result += "NULL"
        return result

    def delete(self, value):
        """
        Deletes the first node containing the given value from the linked list, if it exists.

        Parameters:
        ----------
        value : any
            The value to search for and delete from the linked list.

        Returns:
        -------
        None
        """
        current_node = self.head
        if current_node and current_node.value == value:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

```

### Saif Obeidat