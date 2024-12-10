def load_input():
    input_list = []
    with open("1.data", "r") as data:
        for line in data:
            nums = line.rstrip().split("   ")
            for num in nums:
                input_list.append(int(num))
    return input_list

def make_pair(l1: list[int], l2: list[int]) -> (int, int):
    # Pair smallest in l1 and l2 and remove them from the lists
    s1 = min(l1)
    s2 = min(l2)
    l1.remove(s1)
    l2.remove(s2)
    return (s1, s2)

def get_distance(l1: list[int], l2: list[int]) -> int:
    l1 = l1.copy()
    l2 = l2.copy()
    total_distance = 0

    for i in range(len(l1)):
        pair = make_pair(l1, l2)
        total_distance += abs(pair[0] - pair[1])

    return total_distance


def get_num_occurences(nums, x):
    n_occurences = 0
    for n in nums:
        if n == x:
            n_occurences += 1
    return n_occurences

def main():
    puzzle_in = load_input()

    left_list = [i for i in puzzle_in[0::2]]
    right_list = [i for i in puzzle_in[1::2]]
    total_distance = get_distance(left_list, right_list)

    print(f"distance: {total_distance}")

    sim_score = sum(
        [l * get_num_occurences(right_list, l) for l in left_list]
        )
    print(f"similarity: {sim_score}")



if __name__ == '__main__':
    main()