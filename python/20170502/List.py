class Node:
	next = None
	data = None
	def __init__(self,nodeData):
		self.data = nodeData

class List:
	root = None
	size = 0
	def __init__(self,newRoot):
		self.root = newRoot
	def __init__(self):
		self.root = None
		size = 0

	def __del__(self):
		if self.root is None:
			return
		curNode = self.root
		while curNode.next is not None:
			tempNode = curNode
			curNode = curNode.next
			temNode = Node
			curNode = Node

	def Insert(self,newData):
		newNode = Node(newData)
		if self.root is None:
			self.root = newNode
			return
		tempNode = self.root
		while tempNode.next is not None:
			tempNode = tempNode.next
		tempNode.next = newNode
		self.size += 1

	def Remove(self,theData):
		curNode = self.root
		if curNode is None:
			return
		if self.size == 1 and curNode.data == theData:
			curNode.data = None
			curNode = None
			self.size = -1
			return 
		while curNode.next is not None:
			if curNode.next.data == theData:
				tempNode = curNode.next
				curNode.next = curNode.next.next
				tempNode = None
				self.size = -1
			else:
				curNode = curNode.next
	def GetRoot(self):
		return self.root
	
	def GetSize(self):
		return self.size

	def Print(self):
		tempNode = self.root
		while tempNode is not None:
			print(tempNode.data)
			tempNode = tempNode.next
