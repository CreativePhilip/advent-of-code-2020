import pprint
import string

pp = pprint.PrettyPrinter(indent=4)


def byr(x):
    return len(x) == 4 and (1920 <= int(x) <= 2020)


def iyr(x):
    return len(x) == 4 and (2010 <= int(x) <= 2020)


def eyr(x):
    return len(x) == 4 and (2020 <= int(x) <= 2030)


def hgt(x):
    system = x[-2:]
    print(x[:-2], system, x)
    if system == "cm":
        return 150 <= int(x[:-2]) <= 193
    elif system == "in":
        return 59 <= int(x[:-2]) <= 76


def hcl(x):
    if x[0] == '#':
        return all(c in string.hexdigits for c in x[1:])
    return False


def ecl(x):
    return x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid(x: str):
    return len(x) == 9 and x.isnumeric()


required_keys = {
    "byr": byr,
    "iyr": iyr,
    "eyr": eyr,
    "hgt": hgt,
    "hcl": hcl,
    "ecl": ecl,
    "pid": pid
}


def task1(test=True):
    file_name = "test_passport.txt" if test else "passports.txt"
    with open(file_name, 'r') as file:
        passports = file.read().split("\n\n")
        valid_passports = 0

        for i in passports:
            key_val = i.replace("\n", " ").split(" ")
            keys = [i.split(":")[0] for i in key_val]
            values = [i.split(":")[1] for i in key_val]
            is_valid = all(i in keys for i in required_keys)

            if is_valid and all([required_keys[i](j) for i, j in zip(keys, values) if i != "cid"]):
                valid_passports += 1

        print(f"there are {valid_passports} valid passports")


if __name__ == '__main__':
    task1(False)
