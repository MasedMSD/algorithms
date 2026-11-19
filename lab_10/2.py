def unique_paths(rows, cols):
	dp = [[1] * cols for _ in range(rows)]

	for i in range(1, rows):
		for j in range(1, cols):
			dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

	return dp[rows - 1][cols - 1]


def run_tests():
	tests = [
		(3, 7, 28),  # поле 3x7 -> 28 путей
		(3, 2, 3),  # поле 3x2 -> 3 пути
		(3, 3, 6),  # квадрат 3x3 -> 6 путей
		(1, 5, 1),  # одна строка -> только 1 путь вправо
		(1, 1, 1),  # старт совпадает с финишем -> 1 путь
	]
	for idx, (r, c, expected) in enumerate(tests, 1):
		result = unique_paths(r, c)
		status = "OK" if result == expected else "FAIL"
		print(f"Тест {idx}: поле {r}x{c} -> ответ: {result} (ожидалось: {expected}) [{status}]")


if __name__ == "__main__":
	run_tests()
