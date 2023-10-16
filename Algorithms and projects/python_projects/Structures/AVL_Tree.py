class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class AVL:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, current):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
                current.left.parent = current
                self.inspected_add(current.left)
            else:
                self._add(value, current.left)
            
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
                current.right.parent = current
                self.inspected_add(current.right)
            else:
                self._add(value, current.right)

    def delete_value(self, value):
        return self.delete_node(self.find(value))

    def delete_node(self, node):


        def min_value_node(n):
            current = n
            while current.left:
                current = current.left
            return current

        def num_children(n):
            num_children = 0
            if n.left: num_children+=1
            if n.right: num_children+=1
            return num_children

        node_parent = node.parent
        node_children = num_children(node)

        if node_children == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None

        if node_children == 1:
            if node.left:
                child = node.left
            else:
                child = node.right

            if node_parent.left == node:
                node_parent.left = child
            else:
                node_parent.right = child

            child.parent = node_parent

        if node_children == 2:
            successor=min_value_node(node.right)

            node.value = successor.value
            self.delete_node(successor)    
        
            return

        if node_parent:
            node_parent.height = 1+max(self.get_height(node_parent.left),
            self.get_height(node_parent.right))

            self._inspect_deletion(node_parent)

    def _inspect_deletion(self, current):
        if current == None: return

        left_height = self.get_height(current.left)
        right_height = self.get_height(current.right)

        if abs(left_height - right_height) > 1:
            y = self.taller_child(current)
            x = self.taller_child(y)
            self._rebalance_node(current, y , x)

        self._inspect_deletion(current.parent)

    def inspected_add(self, current, path=[]):
        if current.parent is None: return        
        path = [current] + path

        left_height = self.get_height(current.parent.left)
        right_height = self.get_height(current.parent.right)
    
        
        if abs(left_height - right_height) > 1:
            path = [current.parent] + path
            self._rebalance_node(path[0],path[1],path[2])
            return

        new_height = 1 + current.height
        if current.parent.height < new_height:
            current.parent.height = new_height

        self.inspected_add(current.parent, path)

    def _rebalance_node(self, z, y, x):
        if y == z.left and x == y.left:
            self.right_rotate(z)
        elif y == z.left and x == y.right:
            self.left_rotate(y)
            self.right_rotate(z)
        elif y == z.right and x == y.right:
            self.left_rotate(z)
        elif y == z.right and x == y.left:
            self.right_rotate(y)
            self.left_rotate(z)
        else:
            raise Exception("z, y, x <-- Unknown configuration")

    def right_rotate(self, z):
        sub_root = z.parent
        y = z.left
        t3 = y.right
        z.parent = y
        y.parent = sub_root
        z.left = t3
        if t3:
            t3.parent = z
        y.right = z

        if y.parent == None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def left_rotate(self, z):
        sub_root = z.parent
        y = z.right
        t2 = y.left
        z.parent = y
        y.parent = sub_root
        z.right = t2
        if t2:
            t2.parent = z
        y.left = z
        if y.parent == None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    def get_height(self, node):
        if node == None:
            return 0
        return node.height

    def taller_child(self, current):
        left = self.get_height(current.left)
        right = self.get_height(current.right)
        return current.left if left >= right else current.right

a = AVL()
for i in range(10):
    a.add(i)
print(a.root.value)
print(a.root.left.value)
print(a.root.right.value)
print(a.root.left.left.value)
print(a.root.left.right.value)
print(a.root.right.left.value)
print(a.root.right.right.value)

    #      3
    #    /   \
    #   1     7
    #  / \   / \
    # 0   2 5   8