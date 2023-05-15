from stack_and_queue.stack import Stack

def validate_brackets(str):
    """
    A function that takes a string as its only argument, and returns a boolean representing whether or not the brackets in the string are balanced.
    """

    open_brackets = ["(","{","["]
    close_brackets = [")","}","]"]
    brackets_match = {"{": "}", "[": "]", "(": ")"}

    stack = Stack()

    for char in str:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.is_empty():
                return False
            if brackets_match[stack.pop()] != char:
                return False
            
    if stack.is_empty():
        return True
    else:
        return False




