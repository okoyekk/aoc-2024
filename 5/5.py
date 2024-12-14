import pprint
from collections import defaultdict


def load_input():
    rules = defaultdict(set)
    updates = []
    with open("sample.data", "r") as data:
        for line in data:
            # If line has "|", it is a rule (X|Y) --> Y depends on X
            if "|" in line:
                rule = line.split("|")
                X = int(rule[0])
                Y = int(rule[1])
                rules[Y].add(X)
            # If it has a comma, it is an "update"
            elif "," in line:
                update = [int(u) for u in line.split(",")]
                updates.append(update)

            # If empty, skip
    return rules, updates


def get_valid_update_indices(rules: dict[int, set[int]],
                             updates: list[list[int]]) -> list[int]: 
    # Rules:
    #   X | Y means if X and Y are in an "update", X must come before Y
    # Build adjacency lists with dependencies of form (Y -> {Xs}) for each page
    # For each page(Y) in update(U), ensure all deps(Xs) exist in subset of 
    # U before Y
    # If all pages are valid, add to list and return all
    valid_updates = []
    for i, update in enumerate(updates):
        is_update_invalid = False
        print("************")
        print("update:", update)
        print("------------")
        for j, page in enumerate(update):
            if not is_update_invalid:
                print("page:", page)
                deps = rules[page]
                print("deps:", deps)
                for x in deps:
                    # update is only valid if all dependencies of each page 
                    # come before it
                    print("x:", x)
                    print("update[:j]:", update[:j])
                    if (x in update) and (x not in update[:j]):
                        print("invalid!")
                        is_update_invalid = True
                        break
            else:
                break
        if not is_update_invalid:
            valid_updates.append(i)
    return valid_updates


def get_middle_page(updates: list[int]) -> int:
    return updates[len(updates)//2]


def main():
    data = load_input()
    pprint.pp(data)
    rules = data[0]
    updates = data[1]

    valid = get_valid_update_indices(rules, updates)
    # print("==========")
    # pprint.pp(valid)
    res = 0
    for i in valid:
        res += get_middle_page(updates[i])
    print(res)


if __name__ == '__main__':
    main()
