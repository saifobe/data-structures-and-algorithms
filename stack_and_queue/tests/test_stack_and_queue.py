import pytest
from stack_and_queue.stack import Stack
from stack_and_queue.queue import Queue

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




