class Map:
    def __init__(self, test=False):
        self.map = Map.load_map(test)

    def get(self, x, y):
        if y < 323:
            return self.map[y][x % 31]
        else:
            return "."

    def solve(self, slope):
        pos = (0, 0)
        trees = 0

        for i in range(323):
            cell = self.get(*pos)
            if cell == "#":
                trees += 1
            pos = (pos[0] + slope[0], pos[1] + slope[1])

        print(f"{trees} for slope {slope}")

    def print(self, x, width=1):
        for i in x:
            print(i * width)

    @staticmethod
    def load_map(test=False):
        with open("map.txt", "r") as file:
            return file.read().split("\n")


if __name__ == '__main__':
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    m = Map(True)
    for slope in slopes:
        m.solve(slope)
