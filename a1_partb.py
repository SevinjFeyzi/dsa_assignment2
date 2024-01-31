class DoublyLinked:

	class Node:
		def __init__(self, data, next = None, prev = None):
			self.data = data
			self.next = next
			self.prev = prev

		def get_data(self):
			return self.data

		def get_next(self):
			return self.next

		def get_previous(self):
			return self.prev

	def __init__(self, data = None):
		self.head = None
		self.tail = None
		if data is not None:
			self.push_back(data)

	def get_front(self):
		if self.head is None:
			return None
		return self.head

	def get_back(self):
		if self.tail is None:
			return None
		return self.tail

	def push_front(self, data):
		new_node = self.Node(data)
		if self.head is None:
			self.head = self.tail = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def push_back(self, data):
		new_node = self.Node(data)
		if self.tail is None:
			self.head = self.tail = new_node
		else:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node

	def pop_front(self):
		if self.head is None:
			raise IndexError('pop_front() used on empty list')
		data = self.head.get_data()
		if self.head == self.tail:
			self.head = self.tail = None
		else:
			self.head = self.head.next
			self.head.prev = None
		return data

	def pop_back(self):
		if self.tail is None:
			raise IndexError('pop_back() used on empty list')
		data = self.tail.get_data()
		if self.head == self.tail:
			self.head = self.tail = None
		else:
			self.tail = self.tail.prev
			self.tail.next = None
		return data

	def is_empty(self):
		return self.head is None

	def insert_after(self, data, node):
		#print(data,node.data)
		new_node = self.Node(data)
		if node is None:
			self.push_front(data)
		else:
			new_node.next = node.next
			if node.next is not None:
				node.next.prev = new_node
			node.next = new_node
			new_node.prev = node
		if self.tail == node:
			self.tail = new_node

	def search(self, data):
		current = self.head
		while current is not None:
			if current.get_data() == data:
				return current
			current = current.get_next()
		return None

	def __len__(self):
		count = 0
		current = self.head
		while current is not None:
			count += 1
			current = current.get_next()
		return count

	def is_palindrome(self):
		if self.head is None or self.head.next is None:
			return True

		left = self.head
		right = self.tail
		while left is not None and right is not None:
			if left.get_data() != right.get_data():
				return False
			left = left.next
			right = right.prev
		return True

