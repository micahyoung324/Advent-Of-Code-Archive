FILENAME = "input.txt"


def get_input() -> list[str]:
    banks = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            banks.append(line.strip())

    return banks


def part_1():
    banks = get_input()
    result = 0

    for bank in banks:
        max_jolt = 0
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                this_jolt = int(bank[i] + bank[j])
                if this_jolt >= max_jolt:
                    max_jolt = this_jolt
        result += max_jolt

    print(f"Answer is {result}")


def part_2():
    banks = get_input()
    result = 0

    for bank in banks:
        start_index = 0
        digits = list()

        for d in range(12):
            candidates = [
                (i, bank[i])
                for i in range(start_index, len(bank))
                if i + 11 - d < len(bank)
            ]

            best_index, best_digit = max(candidates, key=lambda t: (t[1], -t[0]))

            next_index = best_index
            digits.append(best_digit)
            start_index = next_index + 1

        result += int("".join(d for d in digits))

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    part_2()
    pass
