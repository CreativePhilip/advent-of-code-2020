from itertools import combinations


def load_data(name):
    with open(name, "r") as file:
        return list(map(int, file.read().split("\n")))


def detect_errors(data, preamble_length):
    for idx, item in enumerate(data):
        if idx in list(range(preamble_length)):
            continue
        data_check = data[idx - preamble_length: idx]

        results = []
        for combination in combinations(data_check, 2):
            results.append(sum(combination) == item)

        if not any(results):
            return item


def detect_errors_2(data, invalid_number):
    for length in range(2, len(data)):
        counter = 0
        while True:
            rng = (counter, counter + length)
            test_values = data[rng[0]: rng[1]]

            if sum(test_values) == invalid_number:
                return min(test_values) + max(test_values)

            counter += 1
            if counter + length > len(data) - 1:
                break


def main():
    inv1 = detect_errors(load_data("test_input.txt"), 5)
    inv2 = detect_errors(load_data("input.txt"), 25)

    print(detect_errors_2(load_data("test_input.txt"), inv1))
    print(detect_errors_2(load_data("input.txt"), inv2))


if __name__ == '__main__':
    main()
