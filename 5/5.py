from collections import defaultdict
import sys
import os

# Get the absolute path of the project root (folder A)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from debug import Debug  # noqa: E402
dbg = Debug(False)


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
        dbg.print("************")
        dbg.print("update:", update)
        dbg.print("------------")
        for j, page in enumerate(update):
            if not is_update_invalid:
                dbg.print("page:", page)
                deps = rules[page]
                dbg.print("deps:", deps)
                for x in deps:
                    # update is only valid if all dependencies of each page 
                    # come before it
                    dbg.print("x:", x)
                    dbg.print("update[:j]:", update[:j])
                    if (x in update) and (x not in update[:j]):
                        dbg.print("invalid!")
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
    dbg.pp(data)
    rules = data[0]
    updates = data[1]

    valid_indices = get_valid_update_indices(rules, updates)
    dbg.print("==========")
    dbg.pp(valid_indices)
    res = 0
    for i in valid_indices:
        res += get_middle_page(updates[i])

    print("result:", res)
    
    # Reorder invalid updates
    invalid_updates = [updates[i] for i in range(len(updates)) 
                       if i not in valid_indices]
    print(invalid_updates)


if __name__ == '__main__':
    main()
