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
            left = self._pre_order(root.left)
            arr2.extend(left)

        if root is not None:
            arr2.append(root.value)

        if root.right is not None:
            right = self._in_order(root.right)
            arr2.extend(right) 
        return arr2
    
    def post_order(self):
        return self._post_order(self.root)
    
    def _post_order(self,root:Node):
        arr3 = []

        if root.left is not None:
            left = self._in_order(root.left)
            arr3.extend(left)

        if root.right is not None:
            right = self._in_order(root.right)
            arr3.extend(right)

        if root is not None:
            arr3.append(root.value)

        return arr3
        
    def maximum(self):
        if self.root is None:
            return None
        else:
            return self._maximum(self.root,maximum = self.root.value)
        
    def _maximum(self,root,maximum):
        
        if root is not None:
            if root.value > maximum:
                maximum = root.value
        
        if root.left is not None:
            maximum = self._maximum(root.left,maximum)

        if root.right is not None:
           maximum = self._maximum(root.right,maximum)
        
        return maximum    

      

class BinarySearchTree(Tree):

    def __init__(self):
        super().__init__()

    def add(self,value):
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
            
    
    def maximum(self):
        if self.root is None:
            return None
        else:
            return self._maximum(self.root)
        
    def _maximum(self,root):
        if root.right is None :
            return root.value
        
        else:
            return self._maximum(root.right)
        








tree1 = Tree()

node1 = Node(5)
tree1.root = node1

node2 = Node(20)
tree1.root.left = node2

node3 = Node(14)
tree1.root.right = node3

node4 = Node(30)
node2.left = node4

node5 = Node(6)
node2.right = node5

print(tree1.maximum())

tree2 = BinarySearchTree()

tree2.add(5)
tree2.add(10)
tree2.add(15)

if 5 in tree2:
    print("True")
else:
    print("False")

print(tree2.Contains(5))
print(tree2.pre_order())
print(tree2.maximum())