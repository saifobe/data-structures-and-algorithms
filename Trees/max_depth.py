from Trees.tree import BinarySearchTree as Tree

def max_depth(root):
    if root is None:
        return 0
    else:
        return max(max_depth(root.left), max_depth(root.right)) + 1
    
if __name__ == "__main__":
    tree = Tree()
    tree.root = tree.add(tree.root, 3)
    tree.root = tree.add(tree.root, 2)
    tree.root = tree.add(tree.root, 1)
    tree.root = tree.add(tree.root, 4)
    tree.root = tree.add(tree.root, 5)
    tree.root = tree.add(tree.root, 6)
    tree.root = tree.add(tree.root, 7)
    tree.root = tree.add(tree.root, 8)

    print(max_depth(tree.root))
