import pytest
from tree_intersection.tree_intersection import tree_intersection
from Trees.tree import Tree,Node

def test_tree_intersection():
    tree1 = Tree()
    tree1.root = Node(5)
    tree1.root.left = Node(10)
    tree1.root.right = Node(15)
    tree1.root.left.left = Node(20)
    tree1.root.left.right = Node(25)
    tree1.root.right.left = Node(30)
    tree1.root.right.right = Node(35)

    tree2 = Tree()
    tree2.root = Node(5)
    tree2.root.left = Node(10)
    tree2.root.right = Node(17)
    tree2.root.left.left = Node(20)
    tree2.root.left.right = Node(26)
    tree2.root.right.left = Node(31)
    tree2.root.right.right = Node(35)

    actual = tree_intersection(tree1,tree2)
    expected = [10, 20, 5, 35]
    assert actual == expected

def test_tree_intersection2():
    tree1 = Tree()
    tree1.root = Node(5)
    tree1.root.left = Node(10)
    tree1.root.right = Node(15)
    

    tree2 = Tree()
    tree2.root = Node(6)
    tree2.root.left = Node(12)
    tree2.root.right = Node(18)
    
    actual = tree_intersection(tree1,tree2)
    expected = []
    assert actual == expected