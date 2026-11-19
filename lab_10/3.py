def max_subarray_sum(nums):
	dp = [0] * len(nums)
	dp[0] = nums[0]

	for i in range(1, len(nums)):
		dp[i] = max(nums[i], dp[i - 1] + nums[i])

	return max(dp)


def run_tests():
	tests = [
		([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # [4, -1, 2, 1] -> сумма 6
		([1, 2, 3, 4], 10),  # весь массив -> 10
		([-5, -2, -8, -1], -1),  # все отрицательные -> максимум -1
		([5, -1, 5], 9),  # выгодно пережить небольшой минус
		([7], 7),  # один элемент
	]
	for idx, (nums, expected) in enumerate(tests, 1):
		result = max_subarray_sum(nums)
		status = "OK" if result == expected else "FAIL"
		print(f"Тест {idx}: nums={nums} -> ответ: {result} (ожидалось: {expected}) [{status}]")


if __name__ == "__main__":
	run_tests()
