# Completed


from collections import deque

graph = {}

edges = [
	("Площадь Восстания", "Владимирская"),
	("Владимирская", "Пушкинская"),
	("Пушкинская", "Технологический институт"),
	("Невский проспект", "Сенная площадь"),
	("Сенная площадь", "Технологический институт"),
	("Гостиный двор", "Маяковская"),
	("Маяковская", "Площадь Александра Невского"),
	("Площадь Александра Невского", "Новочеркасская"),
	("Новочеркасская", "Ладожская"),
	("Ладожская", "Проспект Большевиков"),
	("Адмиралтейская", "Садовая"),
	("Садовая", "Звенигородская"),
	("Звенигородская", "Обводный канал"),
	("Спасская", "Достоевская"),
	("Достоевская", "Лиговский проспект"),
	("Лиговский проспект", "Площадь Александра Невского"),
	("Невский проспект", "Гостиный двор"),
	("Сенная площадь", "Спасская"),
	("Сенная площадь", "Садовая"),
	("Спасская", "Садовая"),
	("Пушкинская", "Звенигородская"),
	("Площадь Восстания", "Маяковская"),
	("Достоевская", "Владимирская"),
]


for a, b in edges:
	graph.setdefault(a, []).append(b)
	graph.setdefault(b, []).append(a)


def bfs(start, end):
	queue = deque([[start]])
	visited = {start}
	while queue:
		path = queue.popleft()
		node = path[-1]
		if node == end:
			return path
		for neighbor in graph[node]:
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append(path + [neighbor])
	return None


def dfs(start, end, visited=None):
	visited = visited or {start}
	if start == end:
		return [start]
	for neighbor in graph[start]:
		if neighbor not in visited:
			visited.add(neighbor)
			path = dfs(neighbor, end, visited)
			if path:
				return [start] + path
	return None


def demo():
	path = bfs("Спасская", "Пушкинская")
	assert path == ["Спасская", "Достоевская", "Владимирская", "Пушкинская"], path
	assert dfs("Спасская", "Пушкинская") is not None
	print("self-check OK")


if __name__ == "__main__":
	demo()
	start = input("Откуда: ").strip()
	end = input("Куда: ").strip()
	path = bfs(start, end)
	print("Выход:", " -> ".join(path) if path else "Станции не связаны")
