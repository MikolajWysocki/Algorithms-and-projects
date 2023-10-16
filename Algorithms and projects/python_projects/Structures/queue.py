
class Queue:
	def __init__(self):
		self.items = [];

	def add(self, value):
		self.items.append(value)

	def pop(self):
		a = self.items.pop(0)
		return a

	def printq(self):
		print(self.items)

	def isEmpty(self):
		return len(self.items)==0

qu = Queue()
qu.add(1)
qu.add(2)
qu.add(3)
qu.add(4)

qu.pop()
print(qu.pop())
qu.printq()
print(qu.isEmpty())
qu.pop()
qu.pop()
print(qu.isEmpty())