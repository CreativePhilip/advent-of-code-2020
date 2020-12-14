from typing import Tuple
from copy import deepcopy


class Map:
    neighbours_conf = [
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1)
    ]

    def __init__(self, name: str):
        self.file_name = name
        self.map = []
        self.last_map = []
        self.load_data()
        self.run(2)

    def load_data(self):
        with open(self.file_name, "r") as file:
            rows = file.read().split("\n")
            response = []
            for i in rows:
                response.append(list(i))
            self.map = response

    def get_neighbours(self, point: Tuple[int, int]) -> list[str]:
        result = []
        for i in self.neighbours_conf:
            new_point = (i[0] + point[0], i[1] + point[1])
            if self.is_point_valid(new_point):
                value = self.map[new_point[0]][new_point[1]]
                if value != ".":
                    result.append(value)
        return result

    def get_neighbours_2(self, point: Tuple[int, int]) -> list[str]:
        result = []
        checked_offsets = []
        current_offset = 1
        while True:
            checked_points = []
            for i in self.neighbours_conf:
                new_point = (i[0] * current_offset + point[0], i[1] * current_offset + point[1])
                if self.is_point_valid(new_point) and i not in checked_offsets:
                    checked_points.append(new_point)
                    value = self.map[new_point[0]][new_point[1]]
                    if value != ".":
                        result.append(value)
                        checked_offsets.append(i)

            if len(checked_points) == 0:
                break

            current_offset += 1
        return result

    def run(self, part):
        while self.map != self.last_map:
            cpy = deepcopy(self.map)
            for col_idx, col in enumerate(self.map):
                for row_idx, cell in enumerate(col):
                    n = self.get_neighbours((col_idx, row_idx)) if part == 1 else self.get_neighbours_2((col_idx, row_idx))

                    if cell == "L" and n.count("#") == 0:
                        cpy[col_idx][row_idx] = "#"
                    elif cell == "#" and n.count("#") >= 5:
                        cpy[col_idx][row_idx] = "L"

            self.last_map = self.map
            self.map = cpy

    def is_point_valid(self, point: Tuple[int, int]) -> bool:
        return 0 <= point[0] < len(self.map) and 0 <= point[1] < len(self.map[0])

    def count_in_map(self, value):
        return sum([i.count(value) for i in self.map])

    def __str__(self):
        result = ""
        for i in self.map:
            result += "".join(i) + "\n"
        return result


def main():
    m = Map("input.txt")
    m.get_neighbours_2((4, 3))
    print(m.count_in_map("#"))


if __name__ == '__main__':
    main()
