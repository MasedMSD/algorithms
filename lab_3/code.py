from collections import Counter


def is_subset(base: list[str], candidate: list[str]) -> bool:
	base_set = set(base)
	return all(item in base_set for item in candidate)


def first_unique_char(s: str) -> str | None:
	counts = Counter(s)

	for ch in s:
		if counts[ch] == 1:
			return ch

	return None


def longest_palindrome(s: str) -> int:
	counts = Counter(s)

	length = 0
	has_odd = False

	for count in counts.values():
		length += count - (count % 2)
		if count % 2 == 1:
			has_odd = True

	return length + 1 if has_odd else length


def build_palindrome(s: str) -> str:
	counts = Counter(s)

	half: list[str] = []
	middle = ""

	for ch, count in counts.items():
		half.append(ch * (count // 2))
		if count % 2 == 1:
			middle = ch

	left = "".join(half)
	return left + middle + left[::-1]


def is_anagram(s: str, t: str) -> bool:
	return Counter(s) == Counter(t)


def main() -> None:
	print("A. Подмножество массива")
	print(is_subset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f"]))
	print(is_subset(["a", "b", "c", "d", "e", "f"], ["b", "d", "f", "h"]))

	print("\nB. Первый неповторяющийся символ")
	print(first_unique_char("minimum"))

	print("\nC. Самый длинный палиндром из букв строки")
	long_case = "abbbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbab"
	palindrome_cases = [
		("aAbBABba", 8),
		("abcdefghijklmnoPQrstuvwxyz", 1),
		("wasitacaroracatisaw", 19),
		("bbbabab", 7),
		("abcdeedcba", 10),
		("looooooongestpalindrOme", 13),
		("abcdeedcbaxyz", 11),
		(long_case, 1122),
	]
	for s, expected in palindrome_cases:
		result = longest_palindrome(s)
		label = s if len(s) <= 30 else f"{s[:15]}...({len(s)} симв.)"
		status = "OK" if result == expected else "FAIL"
		if len(s) <= 30:
			built = build_palindrome(s)
			print(f"{label}: {result} (ожидалось {expected}) {status} | пример палиндрома: {built!r}")
		else:
			print(f"{label}: {result} (ожидалось {expected}) {status}")

	print("\nD. Проверка анаграммы")
	anagram_cases = [
		("нора", "рано", True),
		("монета", "отмена", True),
		("мышка", "камыш", True),
		("тормони", "монитор", True),
		("тоемони", "монитор", False),
	]
	for s, t, expected in anagram_cases:
		result = is_anagram(s, t)
		print(f"{s!r} / {t!r} -> {result} (ожидалось {expected}) {'OK' if result == expected else 'FAIL'}")


if __name__ == "__main__":
	main()
