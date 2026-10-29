class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def build_tree(values):
	if not values:
		return None
	root = TreeNode(values[0])
	queue = [root]
	i = 1
	while queue and i < len(values):
		current = queue.pop(0)
		if i < len(values) and values[i] is not None:
			current.left = TreeNode(values[i])
			queue.append(current.left)
		i += 1
		if i < len(values) and values[i] is not None:
			current.right = TreeNode(values[i])
			queue.append(current.right)
		i += 1
	return root


class SolutionA:
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root:
			return True

		def isMirror(t1, t2):
			if not t1 and not t2:
				return True
			if not t1 or not t2:
				return False
			return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

		return isMirror(root.left, root.right)


class SolutionB:
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		self.diameter = 0

		def depth(node):
			if not node:
				return 0

			left_depth = depth(node.left)
			right_depth = depth(node.right)

			self.diameter = max(self.diameter, left_depth + right_depth)

			return max(left_depth, right_depth) + 1

		depth(root)
		return self.diameter


class SolutionC:
	def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		info = {}

		def dfs(node, parent, depth):
			if not node:
				return
			if node.val == x or node.val == y:
				info[node.val] = (parent, depth)
			dfs(node.left, node, depth + 1)
			dfs(node.right, node, depth + 1)

		dfs(root, None, 0)

		if x in info and y in info:
			parent_x, depth_x = info[x]
			parent_y, depth_y = info[y]
			return depth_x == depth_y and parent_x != parent_y

		return False


tree1 = build_tree([1, 2, 2, 3, 4, 4, 3])
print(SolutionA().isSymmetric(tree1))

tree2 = build_tree([1, 2, 2, None, 3, None, 3])
print(SolutionA().isSymmetric(tree2))

tree3 = build_tree([1, 2, 3, 4, 5])
print(SolutionB().diameterOfBinaryTree(tree3))

tree4 = build_tree([1, 2])
print(SolutionB().diameterOfBinaryTree(tree4))

tree5 = build_tree([1, 2, 3, 4])
print(SolutionC().isCousins(tree5, 4, 3))

tree6 = build_tree([1, 2, 3, None, 4, None, 5])
print(SolutionC().isCousins(tree6, 5, 4))
