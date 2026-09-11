from typing import TypedDict
import random
import time

class Item(TypedDict):
  id: int
  name: str

print("Генерация 1 миллиона товаров...")

n_products = 1000000
sorted_products: list[Item] = [{"id": i, "name": f"Товар_{i}"} for i in range(1, n_products + 1)]

targets = {
    "В начале": 1,
    "В середине": 500000,
    "В конце": 1000000,
    "Случайный": random.randint(1, n_products),
    "Отсутствует": n_products + 1,
}

def linear_search(arr: list[Item], target: int):
    n = len(arr)

    if n == 0:
        return -1

    if arr[0]["id"] == target:
        return 0

    for i in range(n):
        if arr[i]["id"] == target:
            return i

    return -1


def exponential_search(arr: list[Item], target: int):
    n = len(arr)

    if n == 0:
        return -1

    if arr[0]["id"] == target:
        return 0

    i = 1
    while i < n and arr[i]["id"] <= target:
        i = i * 2

    low = i // 2
    high = min(i, n - 1)

    while low <= high:
        mid = (low + high) // 2
        if arr[mid]["id"] == target:
            return mid
        elif arr[mid]["id"] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search(arr: list[Item], target: int):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid]["id"] == target:
            return mid
        elif arr[mid]["id"] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def interpolation_search(arr: list[Item], target: int):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low]["id"] and target <= arr[high]["id"]:
        if low == high:
            if arr[low]["id"] == target:
                return low
            return -1

        pos = low + int(
            (
                (float(high - low) / (arr[high]["id"] - arr[low]["id"]))
                * (target - arr[low]["id"])
            )
        )

        if arr[pos]["id"] == target:
            return pos
        if arr[pos]["id"] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1


algorithms = {
    "Линейный": linear_search,
    "Экспоненц-й": exponential_search,
    "Бинарный": binary_search,
    "Интерполяц-й": interpolation_search,
}

results = {algo: {} for algo in algorithms}

for algo_name, algo_func in algorithms.items():
    for case_name, target_id in targets.items():
        start_time = time.perf_counter()
        algo_func(sorted_products, target_id)
        end_time = time.perf_counter()

        results[algo_name][case_name] = end_time - start_time

print("\n" + "=" * 83)
print(
    f"{'Алгоритм':<13} | {'В начале':<11} | {'В середине':<11} | {'В конце':<11} | {'Случайный':<11} | {'Отсутствует':<11}"
)

for algo_name, times in results.items():
    row_values = [f"{times[case_name]:.6f}s".ljust(11) for case_name in targets.keys()]
    row = f"{algo_name:<13} | " + " | ".join(row_values)
    print(row)
print("=" * 83)
