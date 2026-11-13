LEFT = 0
RIGHT = 1


class Node:
	def __init__(self, key, is_red=True, nil=None):
		self.key = key
		self.is_red = is_red
		self.parent = nil
		self.children = [nil, nil]  # [LEFT, RIGHT]


class RedBlackTree:
	def __init__(self):
		self.NIL = Node(0, is_red=False)
		self.NIL.parent = self.NIL
		self.NIL.children = [self.NIL, self.NIL]
		self.root = self.NIL

	def rotate(self, node, direction):
		"""direction = LEFT (0) для левого поворота, RIGHT (1) для правого."""
		opposite = 1 - direction
		pivot = node.children[opposite]

		node.children[opposite] = pivot.children[direction]
		if pivot.children[direction] != self.NIL:
			pivot.children[direction].parent = node

		pivot.parent = node.parent
		if node.parent == self.NIL:
			self.root = pivot
		else:
			parent_side = int(node == node.parent.children[RIGHT])
			node.parent.children[parent_side] = pivot

		pivot.children[direction] = node
		node.parent = pivot

	def insert(self, key):
		new_node = Node(key, is_red=True, nil=self.NIL)
		parent = self.NIL
		current = self.root

		while current != self.NIL:
			parent = current
			if key == current.key:
				return

			side = int(key > current.key)
			current = current.children[side]

		new_node.parent = parent
		if parent == self.NIL:
			self.root = new_node
		else:
			side = int(key > parent.key)
			parent.children[side] = new_node

		self._fix_insert(new_node)

	def _fix_insert(self, node):
		while node.parent.is_red:
			grandparent = node.parent.parent
			parent_side = int(node.parent == grandparent.children[RIGHT])
			opposite_side = 1 - parent_side
			uncle = grandparent.children[opposite_side]

			if uncle.is_red:
				node.parent.is_red = False
				uncle.is_red = False
				grandparent.is_red = True
				node = grandparent
			else:
				if node == node.parent.children[opposite_side]:
					node = node.parent
					self.rotate(node, parent_side)
				node.parent.is_red = False
				node.parent.parent.is_red = True
				self.rotate(node.parent.parent, opposite_side)

		self.root.is_red = False

	def _replace_node(self, old_node, new_node):
		if old_node.parent == self.NIL:
			self.root = new_node
		else:
			side = int(old_node == old_node.parent.children[RIGHT])
			old_node.parent.children[side] = new_node
		new_node.parent = old_node.parent

	def delete(self, key):
		target = self.root
		while target != self.NIL and target.key != key:
			side = int(key > target.key)
			target = target.children[side]

		if target == self.NIL:
			return

		was_red = target.is_red
		if target.children[LEFT] == self.NIL or target.children[RIGHT] == self.NIL:
			only_child_side = int(target.children[LEFT] == self.NIL)
			replacement = target.children[only_child_side]
			self._replace_node(target, replacement)
		else:
			# Ищем минимальный элемент в правом поддереве
			successor = target.children[RIGHT]
			while successor.children[LEFT] != self.NIL:
				successor = successor.children[LEFT]

			was_red = successor.is_red
			replacement = successor.children[RIGHT]

			if successor.parent == target:
				replacement.parent = successor
			else:
				self._replace_node(successor, replacement)
				successor.children[RIGHT] = target.children[RIGHT]
				successor.children[RIGHT].parent = successor

			self._replace_node(target, successor)
			successor.children[LEFT] = target.children[LEFT]
			successor.children[LEFT].parent = successor
			successor.is_red = target.is_red

		if not was_red:
			self._fix_delete(replacement)

	def _fix_delete(self, node):
		while node != self.root and not node.is_red:
			side = int(node == node.parent.children[RIGHT])
			opposite = 1 - side
			sibling = node.parent.children[opposite]

			if sibling.is_red:
				sibling.is_red = False
				node.parent.is_red = True
				self.rotate(node.parent, side)
				sibling = node.parent.children[opposite]

			if not sibling.children[LEFT].is_red and not sibling.children[RIGHT].is_red:
				sibling.is_red = True
				node = node.parent
			else:
				if not sibling.children[opposite].is_red:
					sibling.children[side].is_red = False
					sibling.is_red = True
					self.rotate(sibling, opposite)
					sibling = node.parent.children[opposite]

				sibling.is_red = node.parent.is_red
				node.parent.is_red = False
				sibling.children[opposite].is_red = False
				self.rotate(node.parent, side)
				node = self.root

		node.is_red = False

	def show(self, node=None, indent="", is_last=True):
		if node is None:
			node = self.root
		if node == self.NIL:
			if node == self.root:
				print("<пусто>")
			return

		branch = "└── " if is_last else "├── "
		color = "R" if node.is_red else "B"
		print(f"{indent}{branch}{node.key} ({color})")

		next_indent = indent + ("    " if is_last else "│   ")
		if node.children[LEFT] != self.NIL or node.children[RIGHT] != self.NIL:
			self.show(node.children[RIGHT], next_indent, False)
			self.show(node.children[LEFT], next_indent, True)


tree = RedBlackTree()
for value in [10, 20, 30, 15, 25, 5, 1]:
	print(f"\n+ Вставка {value}:")
	tree.insert(value)
	tree.show()

for value in [20, 10, 30]:
	print(f"\n- Удаление {value}:")
	tree.delete(value)
	tree.show()
