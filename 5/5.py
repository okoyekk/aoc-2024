from collections import defaultdict
from copy import deepcopy
import sys
import os

# Get the absolute path of the project root (folder A)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from debug import Debug  # noqa: E402
dbg1 = Debug(False)
dbg2 = Debug(False)


def load_input():
    rules = defaultdict(set)
    updates = []
    with open("5.data", "r") as data:
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
        dbg1.print("************")
        dbg1.print("update:", update)
        dbg1.print("------------")
        for j, page in enumerate(update):
            if not is_update_invalid:
                dbg1.print("page:", page)
                deps = rules[page]
                dbg1.print("deps:", deps)
                for x in deps:
                    # update is only valid if all dependencies of each page 
                    # come before it
                    dbg1.print("x:", x)
                    dbg1.print("update[:j]:", update[:j])
                    if (x in update) and (x not in update[:j]):
                        dbg1.print("invalid!")
                        is_update_invalid = True
                        break
            else:
                break
        if not is_update_invalid:
            valid_updates.append(i)
    return valid_updates


def get_middle_page(updates: list[int]) -> int:
    return updates[len(updates)//2]


def get_pages_with_no_incoming_deps(rules: dict[int, set[int]],
                                    update: list[int]) -> set[int]:
    # Find all nodes in update without an incoming edge
    start = set()
    for u in update:
        if len(rules[u]) == 0:
            start.add(u)

    return start


def get_pages_that_depend_on(page: int, rules: dict[int, set[int]]):
    dependent_pages = set()
    # Find all pages that have this page in their dependency set
    for p, deps in rules.items():
        if page in deps:
            dependent_pages.add(p)
    return dependent_pages


def topo_sort(rules: dict[int, set[int]], update: list[int]) -> list[int]:
    # https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
    sorted_updates = []

    # Remove rules depending on pages not in this update and remove rules 
    # for pages that are not in this update
    filtered_rules = deepcopy({p: rules[p] for p in update})
    for page, deps in filtered_rules.items():
        filtered_rules[page] = deps.intersection(update)

    start = get_pages_with_no_incoming_deps(filtered_rules, update)

    while start:
        # Remove page from start and add to sorted update since all its
        # dependencies should be in the list already
        dbg2.print("------START-------")
        dbg2.pp(start)
        page = start.pop()
        sorted_updates.append(page)
        dbg2.pp(sorted_updates)

        for dependent in get_pages_that_depend_on(page, filtered_rules):
            # Remove all dependency on page and if dependent has no other
            # dependencies, add it to start
            filtered_rules[dependent].remove(page)
            if len(filtered_rules[dependent]) == 0:
                start.add(dependent)

    return sorted_updates


def main():
    data = load_input()
    dbg1.pp(data)
    rules = data[0]
    updates = data[1]

    valid_indices = get_valid_update_indices(rules, updates)
    dbg1.print("==========")
    dbg1.pp(valid_indices)
    res_1 = 0
    for i in valid_indices:
        res_1 += get_middle_page(updates[i])

    print("result1:", res_1)
    
    # Reorder invalid updates --- Part 2
    invalid_updates = [updates[i] for i in range(len(updates)) 
                       if i not in valid_indices]
    print("invalid:", invalid_updates)
    dbg2.print("*****rules*****")
    dbg2.pp(rules)
    dbg2.print("***************")

    # Seems like a topological sort ordering problem
    valid_updates = []
    for update in invalid_updates:
        dbg2.print("*******NEW UPDATE********")
        valid_updates.append(topo_sort(rules, update))
    print("valid:", valid_updates)

    res_2 = 0
    for update in valid_updates:
        res_2 += get_middle_page(update)

    print("result2:", res_2)


if __name__ == '__main__':
    main()
