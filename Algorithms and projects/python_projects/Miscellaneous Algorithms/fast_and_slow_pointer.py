###########################################
#
# TIME COMPLEXITY:
#  BIG O(n)
#
# SPACE COMPLEXITY O(1) 
#
###########################################

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

a = Node(5,)
b = Node(7, a)
c = Node(2, b)
d = Node(9, c)
a.next = d
head = Node(1, d)

A = Node(2)
B = Node(2, A)
C = Node(2, B)
head1 = Node(2, C)

#checks if the is a cycle
def HC(head):
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False

print(HC(head))