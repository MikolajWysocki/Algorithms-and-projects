
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self, value):
        node = Node(value, self.head)
        self.head = node

    def print_val(self):
        print(self.head.value)
        if self.head.next:
            self._print_val(self.head.next)

    def _print_val(self, node):
        if node:
            print(node.value)
        if node.next:
            self._print_val(node.next)

    def remove(self, value):
        if self.head.value == value:
            temp = self.head.next
            self.head = temp
        else:
            self._remove(value, self.head.next, self.head)

    def _remove(self, value, current, last):
        if current.value == value:
            last.next = current.next
        else:
            self._remove(value, current.next, current)
          
    def reverse(self):
        self.head = self._reverse(self.head)

    def _reverse(self, head):
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev
        



ls = LinkedList()
ls.add(5)
ls.add(12)
ls.add(3)
ls.add(4)
ls.print_val()
ls.remove(3)
print("")
ls.print_val()
ls.reverse()
print("")
ls.print_val()