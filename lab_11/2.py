class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.dist = 1


class LeftistHeap:
	def __init__(self):
		self.root = None

	def merge_nodes(self, a, b):
		if a is None:
			return b
		if b is None:
			return a
		if a.value > b.value:
			a, b = b, a

		a.right = self.merge_nodes(a.right, b)

		left_dist = a.left.dist if a.left else 0
		right_dist = a.right.dist if a.right else 0
		if left_dist < right_dist:
			a.left, a.right = a.right, a.left

		a.dist = (a.right.dist if a.right else 0) + 1
		return a

	def insert(self, value):
		self.root = self.merge_nodes(self.root, Node(value))

	def get_min(self):
		return None if self.root is None else self.root.value

	def extract_min(self):
		if self.root is None:
			return None
		result = self.root.value
		self.root = self.merge_nodes(self.root.left, self.root.right)
		return result

	def merge(self, *heaps):
		for other in heaps:
			if other is self:
				continue
			self.root = self.merge_nodes(self.root, other.root)
			other.root = None

	def display(self):
		values = []

		def traverse(node):
			if node is None:
				return
			values.append(node.value)
			traverse(node.left)
			traverse(node.right)

		traverse(self.root)
		print(sorted(values))


if __name__ == "__main__":
	left1 = LeftistHeap()
	for x in [10, 4, 15, 2, 8]:
		left1.insert(x)

	print("=== ЛЕВОСТОРОННЯЯ КУЧА ===")
	print("Куча после добавления:")
	left1.display()
	print("Минимальный элемент:", left1.get_min())
	print("Удалённый элемент:", left1.extract_min())
	print("После удаления:")
	left1.display()

	left2 = LeftistHeap()
	for x in [3, 7, 1]:
		left2.insert(x)

	left3 = LeftistHeap()
	for x in [6, 9]:
		left3.insert(x)

	left1.merge(left2, left3)
	print("После слияния трёх куч:")
	left1.display()
