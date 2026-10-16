import heapq

GREEN, PURPLE, BLUE, RED, YELLOW, TRANSFER = 4, 5, 6, 3, 2, 1

graph = {}

edges = [
	("Площадь Восстания", "Владимирская", RED),
	("Владимирская", "Пушкинская", RED),
	("Пушкинская", "Технологический институт", RED),
	("Невский проспект", "Сенная площадь", BLUE),
	("Сенная площадь", "Технологический институт", BLUE),
	("Гостиный двор", "Маяковская", GREEN),
	("Маяковская", "Площадь Александра Невского", GREEN),
	("Адмиралтейская", "Садовая", PURPLE),
	("Садовая", "Звенигородская", PURPLE),
	("Звенигородская", "Обводный канал", PURPLE),
	("Спасская", "Достоевская", YELLOW),
	("Достоевская", "Лиговский проспект", YELLOW),
	("Лиговский проспект", "Площадь Александра Невского", YELLOW),
	("Площадь Александра Невского", "Новочеркасская", YELLOW),
	("Новочеркасская", "Ладожская", YELLOW),
	("Ладожская", "Проспект Большевиков", YELLOW),
	("Невский проспект", "Гостиный двор", TRANSFER),
	("Сенная площадь", "Спасская", TRANSFER),
	("Сенная площадь", "Садовая", TRANSFER),
	("Спасская", "Садовая", TRANSFER),
	("Пушкинская", "Звенигородская", TRANSFER),
	("Площадь Восстания", "Маяковская", TRANSFER),
	("Достоевская", "Владимирская", TRANSFER),
]


for a, b, w in edges:
	graph.setdefault(a, []).append((b, w))
	graph.setdefault(b, []).append((a, w))


def dijkstra(start, end):
	queue = [(0, [start])]
	visited = set()
	while queue:
		time, path = heapq.heappop(queue)
		node = path[-1]
		if node == end:
			return time, path
		if node in visited:
			continue
		visited.add(node)
		for neighbor, w in graph[node]:
			if neighbor not in visited:
				heapq.heappush(queue, (time + w, path + [neighbor]))
	return None


def demo():
	assert dijkstra("Спасская", "Пушкинская") == (
		6,
		["Спасская", "Достоевская", "Владимирская", "Пушкинская"],
	)
	assert dijkstra("Садовая", "Садовая") == (0, ["Садовая"])
	print("self-check OK")


if __name__ == "__main__":
	demo()
	start = input("Откуда: ").strip()
	end = input("Куда: ").strip()
	result = dijkstra(start, end) if start in graph and end in graph else None
	if result:
		time, path = result
		print("Выход:", " -> ".join(path), f"({time} мин)")
	else:
		print("Станции не связаны")
