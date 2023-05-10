import pytest
from stack_and_queue.stack import Stack
from stack_and_queue.queue import Queue
from stack_and_queue.Animal import Animal,Cat,Dog
from stack_and_queue.animal_shelter import AnimalShelter



def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_stack_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_stack_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    assert stack.is_empty()

def test_stack_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.peek() == 3

def test_stack_instantiate_empty():
    stack = Stack()
    assert stack.is_empty()

def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()

def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()

def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1

def test_queue_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.front == None
    assert queue.rear == None

def test_queue_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1
    assert queue.peek() == 1

def test_queue_empty():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()

def test_queue_instantiate_empty():
    queue = Queue()
    assert queue.is_empty()

def test_queue_dequeue_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()

def test_queue_peek_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.peek()


def test_enqueue():
    shelter = AnimalShelter()
    dog1 = Dog("Buddy")
    cat1 = Cat("Whiskers")
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    assert shelter.dogs.peek() == dog1
    assert shelter.cats.peek() == cat1

def test_dequeue():
    shelter = AnimalShelter()
    dog1 = Dog("Buddy")
    cat1 = Cat("Whiskers")
    dog2 = Dog("Max")
    cat2 = Cat("Oliver")
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    shelter.enqueue(dog2)
    shelter.enqueue(cat2)
    assert shelter.dequeue("dog") == dog1
    assert shelter.dequeue("cat") == cat1
    assert shelter.dequeue("dog") == dog2
    assert shelter.dequeue("cat") == cat2
    assert shelter.dequeue("dog") == None
    assert shelter.dequeue("cat") == None

def test_dequeue_with_invalid_preference():
    shelter = AnimalShelter()
    dog1 = Dog("Buddy")
    cat1 = Cat("Whiskers")
    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    assert shelter.dequeue("bird") == None
    assert shelter.dequeue("dog") == dog1
    assert shelter.dequeue("cat") == cat1

def test_animal_attributes():
    dog1 = Dog("Buddy")
    cat1 = Cat("Whiskers")
    assert dog1.name == "Buddy"
    assert dog1.species == "dog"
    assert cat1.name == "Whiskers"
    assert cat1.species == "cat"



