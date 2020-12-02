def part_one():
    with open("inputs.txt", 'r') as file:
        valid_passwords = 0

        for line in file.read().strip().split("\n"):
            rule = line[:line.find(":")]
            password = line[line.find(":") + 2:]
            limits, char = rule.split(" ")
            char_min, char_max = limits.split("-")

            count = 0
            for letter in password:
                if letter == char:
                    count += 1

            if int(char_min) <= count <= int(char_max):
                valid_passwords += 1

        print(f"There are {valid_passwords} valid passwords in the database")


def part_two():
    with open("inputs.txt", 'r') as file:
        valid_passwords = 0

        for line in file.read().strip().split("\n"):
            rule = line[:line.find(":")]
            password = line[line.find(":") + 2:]
            limits, char = rule.split(" ")
            pos1, pos2 = limits.split("-")

            chr1, chr2 = password[int(pos1) - 1], password[int(pos2) - 1]
            if chr1 != chr2 and char in [chr1, chr2]:
                valid_passwords += 1

        print(f"There are {valid_passwords} valid passwords in the database")


if __name__ == '__main__':
    part_one()
    part_two()
