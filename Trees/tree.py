from Trees.node import Node

class Tree:
    def __init__(self):
        self.root = None

    
    def pre_order(self):
        return self._pre_order(self.root)


    def _pre_order(self,root:Node):
        arr = [] 
        if root is None:
            return arr
        
        if root is not None:
            arr.append(root.value)
        
        if root.left is not None:
            left = self._pre_order(root.left)
            arr.extend(left)

        if root.right is not None:
            right = self._pre_order(root.right)
            arr.extend(right)

        return arr
    
    def in_order(self):
        return self._in_order(self.root)
    
    def _in_order(self,root:Node):
        arr2 = []

        if root.left is not None:
            arr2.append(root.left)

        if root is not None:
            head_node = self._in_order(root)
            arr2.extend(head_node)

        if root.right is not None:
            right = self._in_order(root.right)
            arr2.extend(right) 

    def post_order(self):
        return self._post_order(self.root)
    
    def _post_order(self,root:Node):
        arr3 = []

        if root.left is not None:
            arr3.append(root.left)

        if root.right is not None:
            right = self._in_order(root.right)
            arr3.extend(right)

        if root is not None:
            head_node = self._in_order(root)
            arr3.extend(head_node)

         

class BinarySearchTree(Tree):

    def __init__(self):
        super().__init__()

    def Add(self,value):
        if self.root is None:
            self.root = Node(value)  
        else:
            self._Add(self.root,value)
        
        
    def __contains__(self,value):
        return self.Contains(value)
    
    def _Add(self,root,value):
        
        

        if value < root.value:
            if root.left is None:
                root.left = Node(value)
                
            else:
                self._Add(root.left,value)


        if value >= root.value:
            if root.right is None:
                root.right = Node(value)

            else:
                self._Add(root.right,value)

    def Contains(self,value):
        return self._Contains(value,self.root)
        

    def _Contains(self,value,root):

        if root is None:
            return False
        
        if value == root.value:
            return True

        if value < root.value:
            return self._Contains(value,root.left)

        if value >= root.value:
            return self._Contains(value,root.right)
            
        







tree1 = Tree()

node1 = Node("A")
tree1.root = node1

node2 = Node("B")
tree1.root.left = node2

node3 = Node("C")
tree1.root.right = node3

node4 = Node("D")
node2.left = node4

node5 = Node("F")
node2.right = node5

print(tree1.pre_order())

tree2 = BinarySearchTree()

tree2.Add(5)
tree2.Add(10)
tree2.Add(15)

if 5 in tree2:
    print("True")
else:
    print("False")

print(tree2.Contains(5))
print(tree2.pre_order())