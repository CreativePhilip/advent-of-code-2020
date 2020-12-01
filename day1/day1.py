from functools import reduce
from itertools import permutations


def read_numbers():
    with open('day1/numbers.num', 'r') as file:
        return list(map(int, file.read().strip().split("\n")))


def find_pair(numbers: list[int], depth: int):
    for subset in permutations(numbers, depth):
        if sum(subset) == 2020:
            return reduce(lambda a, b: a*b, subset)


if __name__ == '__main__':
    nums = read_numbers()
    result = find_pair(numbers=nums, depth=3)
    print(f"result: {result}")
