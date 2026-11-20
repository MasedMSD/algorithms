import heapq


def select_activities(activities):
	sorted_activities = sorted(activities, key=lambda activity: activity[1])

	selected = []
	last_end_time = 0

	for start, end in sorted_activities:
		if start >= last_end_time:
			selected.append((start, end))
			last_end_time = end

	return selected


def fractional_knapsack(items, capacity):
	sorted_items = sorted(items, key=lambda item: item[0] / item[1], reverse=True)

	total_value = 0.0
	remaining_capacity = capacity

	for value, weight in sorted_items:
		if remaining_capacity == 0:
			break

		if weight <= remaining_capacity:
			total_value += value
			remaining_capacity -= weight
		else:
			fraction = remaining_capacity / weight
			total_value += value * fraction
			remaining_capacity = 0

	return total_value


def min_connection_cost(cables):
	if len(cables) <= 1:
		return 0

	heap = list(cables)
	heapq.heapify(heap)

	total_cost = 0

	while len(heap) > 1:
		first_shortest = heapq.heappop(heap)
		second_shortest = heapq.heappop(heap)

		merged_length = first_shortest + second_shortest
		total_cost += merged_length

		heapq.heappush(heap, merged_length)

	return total_cost


if __name__ == "__main__":
	activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
	chosen_activities = select_activities(activities)
	print("Задача A:")
	print(f"Выбранные активности ({len(chosen_activities)} шт.): {chosen_activities}\n")

	items = [(60, 10), (100, 20), (120, 30)]
	max_weight = 50
	max_value = fractional_knapsack(items, max_weight)
	print("Задача B:")
	print(f"Максимальная стоимость в рюкзаке: {max_value}\n")

	cables = [4, 3, 2, 6]
	cost = min_connection_cost(cables)
	print("Задача C:")
	print(f"Минимальная стоимость соединения: {cost}")
