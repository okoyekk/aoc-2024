import re

def load_input():
	with open("3.data", "r") as data:
		return data.read()

def main():
	query = load_input()
	# print(query)

	# Regex should match something like "mul(<INT>,<INT>)"
	pattern = r"mul\((\d+),(\d+)\)"
	match_groups = re.findall(pattern, query)
	# print(match_groups)

	pairs = [(int(x), int(y)) for x, y in match_groups]
	
	result = sum(x * y for x, y in pairs)

	print(result)


if __name__ == '__main__':
	main()