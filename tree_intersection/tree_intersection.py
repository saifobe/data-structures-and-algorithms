from hash_table.hash_table import Hashtable
from Trees.tree import Tree,Node

def tree_intersection(first,sec):
    hash = Hashtable()
    commen = []

    tree1 = first.in_order()
    tree2 = sec.in_order()

    for node in tree1:
        hash.set(node,True)

    for node2 in tree2:
        if hash.has(node2):
            commen.append(node2)
    return commen
        
if __name__ == "__main__":
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

    print(tree_intersection(tree1,tree2))