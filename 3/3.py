import re

def load_input():
	with open("3.data", "r") as data:
		return data.read()

def mul_1(query: str) -> int:
	# Regex should match something like "mul(<INT>,<INT>)"
	pattern = r"mul\((\d+),(\d+)\)"
	match_groups = re.findall(pattern, query)
	# print(match_groups)

	pairs = [(int(x), int(y)) for x, y in match_groups]
	
	return sum(x * y for x, y in pairs)

def mul_2(query: str) -> int:
	# Regex should catch old query plus do() and undo()
	pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
	match_groups = re.findall(pattern, query)
	# print(match_groups)

	do = True
	total = 0
	# Each pair looks like - (mul(<INT1>,<INT2), INT1, INT2) OR (do(), , )...
	for pair in match_groups: 
		if pair[0] == "do()":
			do = True
		elif pair[0] == "don't()":
			do = False
		else:
			if do:
				num_1, num_2 = int(pair[1]), int(pair[2])
				total += num_1 * num_2

	return total


def main():
	query = load_input()
	# print(query)
	result_1 = mul_1(query)
	print(result_1)

	result_2 = mul_2(query)
	print(result_2)


if __name__ == '__main__':
	main()