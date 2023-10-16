
import queue

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, current):
        if value < current.value:
            if current.left == None:
                current.left = Node(value)
            else:
                self._add(value, current.left)
                
        elif value > current.value:
            if current.right == None:
                current.right = Node(value)
            else:
                self._add(value, current.right)
        else:
            print("obiekt już się znajduje w drzewku")

    def find(self, value):
        if self.root == None:
            return "Empty Tree"
        else:
            if self.root.value == value:
                return True
            else:
                if self._find(value, self.root):
                    return True
                else:
                    return False

    def _find(self, value, current):
        if value < current.value and current.left:
            return self._find(value, current.left)
        elif value > current.value and current.right:
            return self._find(value, current.right)
        if value == current.value:
            return True

    def traverse(self):
        current = self.root
        #changeable
        self.preorder(current)
        
    def visit(self, node):
        print(node.value)

    def preorder(self, current):
        self.visit(current)
        if current.left:
            self.preorder(current.left)
        if current.right:
            self.preorder(current.right)

    def inorder(self, current):
        if current.left:
            self.inorder(current.left)
        self.visit(current)
        if current.right:
            self.inorder(current.right)

    def postorder(self, current):
        if current.left:
            self.postorder(current.left)
        if current.right:
            self.postorder(current.right)
        self.visit(current)

    def BFS(self):
        current = self.root
        qu = queue.Queue()
        qu.put(current)
        self._BFS(qu)

    def _BFS(self, qu):
        temp = qu.get()
        self.visit(temp)
        if temp.left:
            qu.put(temp.left)
        if temp.right:
            qu.put(temp.right)
        if qu.empty() == False:
            self._BFS(qu)
        

Tree = BST()
Tree.add(5)
Tree.add(7)
Tree.add(6)
Tree.add(3)
Tree.add(9)
# print(Tree.find(12))
# Tree.BFS()
Tree.traverse()

#       5
#      / \       
#     3   7
#        / \
#       6   9