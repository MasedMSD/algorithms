class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.red = True


class RedBlackTree:
	def __init__(self):
		self.root = None

	def is_red(self, node):
		return node is not None and node.red

	def rotate_left(self, node):
		new_root = node.right
		node.right = new_root.left
		new_root.left = node

		new_root.red = node.red
		node.red = True
		return new_root

	def rotate_right(self, node):
		new_root = node.left
		node.left = new_root.right
		new_root.right = node

		new_root.red = node.red
		node.red = True
		return new_root

	def flip_colors(self, node):
		node.red = not node.red
		node.left.red = not node.left.red
		node.right.red = not node.right.red

	def insert(self, value):
		self.root = self._insert(self.root, value)
		self.root.red = False

	def _insert(self, node, value):
		if node is None:
			return Node(value)

		if value < node.value:
			node.left = self._insert(node.left, value)
		elif value > node.value:
			node.right = self._insert(node.right, value)
		else:
			return node

		# Балансировка дерева
		if self.is_red(node.right) and not self.is_red(node.left):
			node = self.rotate_left(node)

		if self.is_red(node.left) and self.is_red(node.left.left):
			node = self.rotate_right(node)

		if self.is_red(node.left) and self.is_red(node.right):
			self.flip_colors(node)

		return node

	def get_values(self, node):
		if node is None:
			return []

		return self.get_values(node.left) + [node.value] + self.get_values(node.right)

	def delete(self, value):
		values = self.get_values(self.root)
		self.root = None

		for number in values:
			if number != value:
				self.insert(number)

	def show(self, node=None, level=0):
		if node is None:
			if level == 0:
				node = self.root
			if node is None:
				return

		self.show(node.right, level + 1)

		color = "R" if node.red else "B"
		print("    " * level + f"{node.value} ({color})")

		self.show(node.left, level + 1)


tree = RedBlackTree()

for value in [10, 20, 30, 15, 25, 5, 1]:
	tree.insert(value)

print("После вставки:")
tree.show()

tree.delete(20)

print("\nПосле удаления 20:")
tree.show()
