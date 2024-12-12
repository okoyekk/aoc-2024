def load_input():
    input_list = []
    with open("/Users/kenechi/Desktop/aoc-2024/2/2.data", "r") as data:
        for report in data:
            levels = report.rstrip().split(" ")
            levels = [int(l) for l in levels]
            input_list.append(levels)
    return input_list

def is_report_safe_1(report):
    if len(report) <= 1:
        return True
    # Check if list is decreasing, if so make it negative so it is increasing
    lst = report.copy()
    if lst[0] >= lst[1]:
        lst = [-i for i in lst]

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]: # must be monotonic
            return False
        diff = abs(lst[i] - lst[i + 1])
        if not 1 <= diff <= 3:
            return False

    return True

def compute_diffs(input_list):
    if len(input_list) < 2:
        return []  # Return an empty list if there are less than 2 elements
    
    return [input_list[i] - input_list[i + 1] for i in range(len(input_list) - 1)]


def is_report_safe_2(report):
    if len(report) <= 1:
        return True
    # Check if list is decreasing, if so make it negative so it is increasing
    lst = report.copy()
    if lst[0] >= lst[1] >= lst[2]:
        lst = [-i for i in lst]

    removed = False
    replaced = False
    last_removed_level = 0
    last_removed_level_pos = -1
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])

        if (lst[i] > lst[i + 1]) or (not 1 <= diff <= 3):
            # Check if report is safe if we remove this level
            report_without_current = [x for ind, x in enumerate(lst) if ind != i]
            if removed:
                # Return false only if the report is still unsafe when we remove
                # the current level and reinsert the previously removed level
                report_with_removed_level_added = report_without_current.copy()
                report_with_removed_level_added.insert(last_removed_level_pos, last_removed_level)
                if not is_report_safe_1(report_with_removed_level_added):
                    # print("unsafe:", lst, "-->", compute_diffs(lst))
                    return False
                else:
                    last_removed_level_pos = i
                    last_removed_level = lst[i]
                    replaced = True
            else:
                if not is_report_safe_1(report_without_current):
                    # print("removed:", lst[i], "@", i, "in", lst)
                    removed = True
                    last_removed_level_pos = i
                    last_removed_level = lst[i]
    if replaced:
        return False

    return True


def main():
    data = load_input()
    # print(data)

    n_safe_1 = 0
    for report in data:
        if is_report_safe_1(report):
            n_safe_1 += 1
    print(f"safe_1 reports: {n_safe_1}") # --> 624

    n_safe_2 = 0
    for report in data:
        if is_report_safe_2(report):
            n_safe_2 += 1
    print("-----------------------------")
    print(f"safe_2 reports: {n_safe_2}") # --> 641

    # Notes: Came pretty close to solution (between 657 and 661?) but ended up
    # giving up on this. Code is starting to get messy


if __name__ == '__main__':
    main()