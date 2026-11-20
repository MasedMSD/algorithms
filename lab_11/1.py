class BinaryHeap:
	def __init__(self):
		self.heap = []

	def insert(self, value):
		self.heap.append(value)
		i = len(self.heap) - 1

		while i > 0:
			parent = (i - 1) // 2
			if self.heap[parent] <= self.heap[i]:
				break
			self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
			i = parent

	def get_min(self):
		if not self.heap:
			return None
		return self.heap[0]

	def extract_min(self):
		if not self.heap:
			return None

		result = self.heap[0]
		last = self.heap.pop()
		if not self.heap:
			return result

		self.heap[0] = last
		i = 0
		n = len(self.heap)
		while True:
			left = 2 * i + 1
			right = 2 * i + 2
			smallest = i

			if left < n and self.heap[left] < self.heap[smallest]:
				smallest = left
			if right < n and self.heap[right] < self.heap[smallest]:
				smallest = right
			if smallest == i:
				break

			self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
			i = smallest

		return result

	def merge(self, *heaps):
		for other in heaps:
			for value in list(other.heap):
				self.insert(value)

	def display(self):
		print(self.heap)


if __name__ == "__main__":
	heap1 = BinaryHeap()
	for x in [10, 4, 15, 2, 8]:
		heap1.insert(x)

	print("=== ДВОИЧНАЯ КУЧА ===")
	print("Куча после добавления:")
	heap1.display()
	print("Минимальный элемент:", heap1.get_min())
	print("Удалённый элемент:", heap1.extract_min())
	print("После удаления:")
	heap1.display()

	heap2 = BinaryHeap()
	for x in [3, 7, 1]:
		heap2.insert(x)

	heap3 = BinaryHeap()
	for x in [6, 9]:
		heap3.insert(x)

	heap1.merge(heap2, heap3)
	print("После слияния трёх куч:")
	heap1.display()
