from itertools import permutations


def load_data(name):
    with open(name, "r") as file:
        return list(map(int, file.read().split("\n")))


def solve_1(data):
    diffs = []
    s_data = list(sorted(data))
    for idx, item in enumerate(s_data):
        if idx == 0:
            continue
        diffs.append(item - s_data[idx - 1])
    print((diffs.count(1) + 1) * (diffs.count(3) + 1))


def return_drops(data):
    data.append(0)
    data.append(max(data) + 3)  # This is kinda bad
    ans = []
    max_path = list(sorted(data))
    for idx, item in enumerate(max_path):
        if idx == 0 or idx == len(data) - 1:
            continue

        if max_path[idx + 1] - max_path[idx - 1] <= 3:
            ans.append(item)

    return ans


def calculate_paths(data, drops):
    s_data = list(sorted(data))

    print(list(permutations(drops)))


def main():
    d1 = load_data("test.txt")
    # solve_1(d1)
    # solve_1(load_data("input.txt"))

    drop1 = return_drops(d1)
    calculate_paths(d1, drop1)

if __name__ == '__main__':
    main()
