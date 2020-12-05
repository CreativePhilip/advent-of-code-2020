import math


def binary_search(pattern):
    current_row_range = (0, 127)
    current_column_range = (0, 7)
    row = None
    column = None

    for i in pattern[:7]:
        delta = abs(current_row_range[0] - current_row_range[1]) / 2
        if i == "F":
            current_row_range = (current_row_range[0], current_row_range[1] - delta)
        else:
            current_row_range = (current_row_range[0] + delta, current_row_range[1])
        row = min(current_row_range)

    for j in pattern[7:]:
        delta = abs(current_column_range[0] - current_column_range[1]) / 2
        if j == "L":
            current_column_range = (current_column_range[0], current_column_range[1] - delta)
        else:
            current_column_range = (current_column_range[0] + delta, current_column_range[1])
        column = max(current_column_range)

    return (math.ceil(row) * 8) + math.floor(column)


def task1():
    with open("places.txt", "r") as file:
        x = file.read().split("\n")
        ans = []
        for i in x:
            ans.append(binary_search(i))

        ans = sorted(ans)

        for idx, item in enumerate(ans):
            if idx == 0:
                continue

            if item != ans[idx - 1] + 1:
                print(ans[idx - 1], item, ans[idx + 1])


if __name__ == '__main__':
    task1()

    # (binary_search("FBFBBFFRLR"))
    # (binary_search("BFFFBBFRRR"))
    # (binary_search("FFFBBBFRRR"))
    # (binary_search("BBFFBBFRLL"))
