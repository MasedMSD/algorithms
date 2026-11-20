def longest_increasing_segment(nums):
	if not nums:
		return 0

	dp = [1] * len(nums)

	for i in range(1, len(nums)):
		if nums[i] > nums[i - 1]:
			dp[i] = dp[i - 1] + 1

	return max(dp)


if __name__ == "__main__":
	tests = [
		([1, 3, 5, 4, 7], 3),
		([2, 2, 2, 2], 1),
		([1, 2, 3, 4, 5], 5),
		([5, 4, 3, 2, 1], 1),
		([], 0),
	]
	for idx, (nums, expected) in enumerate(tests, 1):
		result = longest_increasing_segment(nums)
		status = "OK" if result == expected else "FAIL"
		print(f"Тест {idx}: nums={nums} -> ответ: {result} (ожидалось: {expected}) [{status}]")
