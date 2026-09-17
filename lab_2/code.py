import random
import time
from typing import TypedDict


class Item(TypedDict):
	id: int
	name: str


class Request(TypedDict):
	ip: str
	status: int


def generate_products(n: int) -> list[Item]:
	ids = list(range(1, n + 1))
	random.shuffle(ids)

	return [{"id": i, "name": f"Товар_{i}"} for i in ids]


def bubble_sort(arr: list[Item]) -> list[Item]:
	arr = arr[:]
	n = len(arr)

	for i in range(n - 1):
		swapped = False

		for j in range(n - 1 - i):
			if arr[j]["id"] > arr[j + 1]["id"]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				swapped = True

		if not swapped:
			break

	return arr

def insertion_sort(arr: list[Item]) -> list[Item]:
	arr = arr[:]

	for i in range(1, len(arr)):
		current = arr[i]
		j = i - 1

		while j >= 0 and arr[j]["id"] > current["id"]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = current

	return arr


def quick_sort(arr: list[Item]) -> list[Item]:
	arr = arr[:]

	def _sort(low: int, high: int) -> None:
		while low < high:
			pivot_idx = random.randint(low, high)
			arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
			pivot = arr[high]["id"]

			i = low
			for j in range(low, high):
				if arr[j]["id"] < pivot:
					arr[i], arr[j] = arr[j], arr[i]
					i += 1
			arr[i], arr[high] = arr[high], arr[i]

			if i - low < high - i:
				_sort(low, i - 1)
				low = i + 1
			else:
				_sort(i + 1, high)
				high = i - 1

	_sort(0, len(arr) - 1)
	return arr


def generate_requests(n: int) -> list[Request]:
	statuses = [200, 200, 200, 301, 404, 404, 500, 502]
	requests: list[Request] = []

	for _ in range(n):
		ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
		requests.append({"ip": ip, "status": random.choice(statuses)})

	attacker_ip = "13.13.13.13"
	for _ in range(n // 10):
		requests.append({"ip": attacker_ip, "status": 200})

	return requests


def counting_sort_by_status(requests: list[Request]) -> list[Request]:
	low, high = 100, 599
	buckets: list[list[Request]] = [[] for _ in range(high - low + 1)]

	for req in requests:
		buckets[req["status"] - low].append(req)

	result: list[Request] = []
	for bucket in buckets:
		result.extend(bucket)

	return result


def _ip_to_int(ip: str) -> int:
	octets = ip.split(".")
	value = 0

	for octet in octets:
		value = (value << 8) | int(octet)

	return value


def radix_sort_by_ip(requests: list[Request]) -> list[Request]:
	arr = requests[:]

	for byte_index in range(4):
		shift = byte_index * 8
		buckets: list[list[Request]] = [[] for _ in range(256)]

		for req in arr:
			digit = (_ip_to_int(req["ip"]) >> shift) & 0xFF
			buckets[digit].append(req)

		arr = [req for bucket in buckets for req in bucket]

	return arr


def main() -> None:
	print("Генерация 1 миллиона товаров (неотсортированных)...")
	n_products = 1_000_000
	products = generate_products(n_products)

	n_simple = 5_000
	simple_sample = products[:n_simple]

	simple_algorithms = {
		"Пузырьковая": bubble_sort,
		"Вставками": insertion_sort,
	}
	fast_algorithms = {
		"Быстрая (Quick)": quick_sort,
	}

	results: dict[str, tuple[float, int]] = {}

	for name, func in simple_algorithms.items():
		start = time.perf_counter()
		func(simple_sample)
		end = time.perf_counter()
		results[name] = (end - start, n_simple)

	for name, func in fast_algorithms.items():
		start = time.perf_counter()
		func(products)
		end = time.perf_counter()
		results[name] = (end - start, n_products)

	print("\n" + "=" * 55)
	print(f"{'Алгоритм':<17} | {'N элементов':<12} | {'Время':<10}")
	for name, (elapsed, n) in results.items():
		print(f"{name:<17} | {n:<12} | {elapsed:.6f}s")
	print("=" * 55)

	print("\nГенерация 10 000 запросов к серверу...")
	requests = generate_requests(10_000)

	start = time.perf_counter()
	by_status = counting_sort_by_status(requests)
	counting_time = time.perf_counter() - start

	start = time.perf_counter()
	by_ip = radix_sort_by_ip(requests)
	radix_time = time.perf_counter() - start

	status_counts: dict[int, int] = {}
	for req in by_status:
		status_counts[req["status"]] = status_counts.get(req["status"], 0) + 1

	ip_counts: dict[str, int] = {}
	for req in by_ip:
		ip_counts[req["ip"]] = ip_counts.get(req["ip"], 0) + 1

	threshold = 100
	suspects = {ip: c for ip, c in ip_counts.items() if c > threshold}

	print("\n" + "=" * 55)
	print(f"{'Метод':<20} | {'N':<8} | {'Время':<10}")
	print(f"{'Counting Sort (status)':<20} | {len(requests):<8} | {counting_time:.6f}s")
	print(f"{'Radix Sort (ip)':<20} | {len(requests):<8} | {radix_time:.6f}s")
	print("=" * 55)

	print("\nЗапросы по HTTP-статусам:")
	for status, count in sorted(status_counts.items()):
		print(f"  {status}: {count}")

	print(f"\nПодозрительные IP (> {threshold} запросов/сек) — возможная DDoS-атака:")
	for ip, count in sorted(suspects.items()):
		print(f"  {ip}: {count} запросов")


if __name__ == "__main__":
	main()
