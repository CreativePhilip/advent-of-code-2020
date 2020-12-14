"""
0 - NORTH
1 - EAST
2 - SOUTH
3 - WEST
"""
from pprint import pprint


class Ship:
    orientation = 1
    position = (0, 0)

    def __init__(self, name):
        self.name = name

        self.load_instructions()

    def manhattan(self):
        return abs(self.position[0]) + abs(self.position[1])

    def run(self):
        for i in self.load_instructions():
            if i[0] in ["L", "R"]:
                self.execute_rotation(i)
            elif i[0] in ["N", "E", "S", "W"]:
                self.execute_global_move(i)
            elif i[0] in ["F"]:
                self.execute_relative_move(i)
            else:
                print("Invalid move")

            # input()

    def load_instructions(self):
        with open(self.name, "r") as file:
            ins = file.read().split("\n")
            parsed_ins = []

            for i in ins:
                parsed_ins.append((i[0], int(i[1:])))

            return parsed_ins

    def execute_global_move(self, cmd):
        direction = cmd[0]
        if direction == "N":
            self.position = self.position = (self.position[0], self.position[1] + cmd[1])
        elif direction == "E":
            self.position = (self.position[0] + cmd[1], self.position[1])
        elif direction == "S":
            self.position = (self.position[0], self.position[1] - cmd[1])
        elif direction == 'W':
            self.position = (self.position[0] - cmd[1], self.position[1])

    def execute_relative_move(self, cmd):
        if self.orientation == 0:
            self.position = (self.position[0], self.position[1] + cmd[1])
        elif self.orientation == 1:
            self.position = (self.position[0] + cmd[1], self.position[1])
        elif self.orientation == 2:
            self.position = (self.position[0], self.position[1] - cmd[1])
        elif self.orientation == 3:
            self.position = (self.position[0] - cmd[1], self.position[1])

    def execute_rotation(self, cmd):
        value = cmd[1] // 90

        if cmd[0] == "L":
            value *= -1

        print(f"Rotation cmd: {cmd}, old: {self.orientation}, new: {(self.orientation + value) % 4}")
        self.orientation = (self.orientation + value) % 4


if __name__ == '__main__':
    s = Ship("input.txt")
    # pprint(s.load_instructions())
    s.run()
    print(s.manhattan())
