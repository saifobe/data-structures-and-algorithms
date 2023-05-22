import pytest
from Trees.node import Node
from Trees.tree import Tree , BinarySearchTree

def test_empty_tree():
    tree = BinarySearchTree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_add_one_node():
    tree = BinarySearchTree()
    tree.add(5)
    actual = tree.root.value
    expected = 5
    assert actual == expected

def test_add_two_nodes():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    actual = tree.root.left.value
    expected = 3
    assert actual == expected

def test_add_three_nodes():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    actual = tree.root.right.value
    expected = 7
    assert actual == expected

def test_add_four_nodes():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(4)
    actual = tree.root.left.right.value
    expected = 4
    assert actual == expected

def test_add_five_nodes():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(4)
    tree.add(6)
    actual = tree.root.right.left.value
    expected = 6
    assert actual == expected


def test_contains_true():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(4)
    tree.add(6)
    actual = 7 in tree
    expected = True
    assert actual == expected

def test_contains_false():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(4)
    tree.add(6)
    actual = 8 in tree
    expected = False
    assert actual == expected

def test_contains_empty_tree():
    tree = BinarySearchTree()
    actual = 8 in tree
    expected = False
    assert actual == expected

def test_pre_order():
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    actual = tree.pre_order()
    expected = [1,2,3]
    assert actual == expected

def test_in_order():
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    actual = tree.in_order()
    expected = [2,1,3]
    assert actual == expected

def test_post_order():
    tree = Tree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    actual = tree.post_order()
    expected = [2,3,1]
    assert actual == expected

def test_max_value():
    tree = Tree()
    tree.root = Node(10)
    tree.root.left = Node(27)
    tree.root.right = Node(100)
    actual = tree.maximum()
    expected = 100
    assert actual == expected

def test_max_value_2():
    tree = Tree()
    tree.root = Node(0.4)
    tree.root.left = Node(0.10)
    tree.root.right = Node(0.1)
    actual = tree.maximum()
    expected = 0.4
    assert actual == expected


def test_max_value_empty_tree():
    tree = Tree()
    actual = tree.maximum()
    expected = None
    assert actual == expected

