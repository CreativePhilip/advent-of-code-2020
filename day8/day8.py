def load_rom(file_name):
    file = open(file_name, "r")

    instructions = file.read().split("\n")
    ir = []
    for ins in instructions:
        code, value = ins.split(" ")
        ir.append((code, int(value)))
    return ir


def run_rom_until_loop(instructions):
    acc = 0
    ip = 0
    visited_instructions = []

    while True:
        if ip >= len(instructions):
            return acc, False

        ins, value = instructions[ip]

        if ip in visited_instructions:
            return acc, True
        visited_instructions.append(ip)

        if ins == "nop":
            pass
        elif ins == "acc":
            acc += value
        elif ins == "jmp":
            ip += value
            continue

        ip += 1


def fix_corrupted_rom(instructions):
    for idx, _ in enumerate(instructions):
        instructions_cpy = instructions[:]
        if instructions_cpy[idx][0] == "nop":
            instructions_cpy[idx] = ("jmp", instructions_cpy[idx][1])
        elif instructions_cpy[idx][0] == "jmp":
            instructions_cpy[idx] = ("nop", instructions_cpy[idx][1])

        acc, f = run_rom_until_loop(instructions_cpy)
        if not f:
            print(f"Accumulator value after correction: {acc}")


if __name__ == '__main__':
    rom_test = load_rom("test_rom_1.txt")
    acc_value, fail = run_rom_until_loop(rom_test)
    print(f"Accumulator value: {acc_value}  ROM: TEST 1  FAILED: {fail}")
    fix_corrupted_rom(rom_test)

    rom = load_rom("rom_1.txt")
    acc_value, fail = run_rom_until_loop(rom)
    print(f"Accumulator value: {acc_value}  ROM: TASK 1  FAILED: {fail}")
    fix_corrupted_rom(rom)
