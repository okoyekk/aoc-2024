def load_input():
    input_list = []
    with open("2.data", "r") as data:
        for report in data:
            levels = report.rstrip().split(" ")
            levels = [int(l) for l in levels]
            input_list.append(levels)
    return input_list

def is_report_safe(report):
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


def main():
    data = load_input()
    # print(data)

    n_safe = 0
    for report in data:
        if is_report_safe(report):
            n_safe += 1
    print(f"safe reports: {n_safe}")


if __name__ == '__main__':
    main()