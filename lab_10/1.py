def max_robbery(houses):
	if not houses:
		return 0
	if len(houses) == 1:
		return houses[0]

	dp = [0] * len(houses)
	dp[0] = houses[0]
	dp[1] = max(houses[0], houses[1])

	for i in range(2, len(houses)):
		dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])

	return dp[-1]


def run_tests():
	tests = [
		([1, 2, 3, 1], 4),  # 1 + 3 = 4
		([2, 7, 9, 3, 1], 12),  # 2 + 9 + 1 = 12
		([5, 1, 1, 5], 10),  # 5 + 5 = 10 (пропускаем два дома подряд)
		([10], 10),  # один дом
		([], 0),  # нет домов
	]
	for idx, (houses, expected) in enumerate(tests, 1):
		result = max_robbery(houses)
		status = "OK" if result == expected else "FAIL"
		print(f"Тест {idx}: houses={houses} -> ответ: {result} (ожидалось: {expected}) [{status}]")


if __name__ == "__main__":
	run_tests()
