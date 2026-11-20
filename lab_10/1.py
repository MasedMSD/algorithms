def min_operations(n):
	dp = [0] * (n + 1)

	for i in range(2, n + 1):
		dp[i] = dp[i - 1] + 1
		if i % 2 == 0:
			dp[i] = min(dp[i], dp[i // 2] + 1)
		if i % 3 == 0:
			dp[i] = min(dp[i], dp[i // 3] + 1)

	return dp[n]


if __name__ == "__main__":
	tests = [
		(1, 0),
		(5, 3),
		(8, 3),
		(10, 3),
		(96234, 14),
	]
	for idx, (n, expected) in enumerate(tests, 1):
		result = min_operations(n)
		status = "OK" if result == expected else "FAIL"
		print(f"Тест {idx}: n={n} -> ответ: {result} (ожидалось: {expected}) [{status}]")
