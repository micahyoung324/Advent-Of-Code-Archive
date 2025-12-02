FILENAME = "input.txt"


def is_valid1(num: int) -> bool:
    num_str = str(num)

    if len(num_str) % 2 == 1:
        return True

    half_length = len(num_str) // 2

    first_num_str = num_str[:half_length]
    second_num_str = num_str[half_length:]

    return first_num_str != second_num_str


def is_valid2(num: int) -> bool:
    num_str = str(num)

    if len(num_str) == 1:
        return True

    if len(num_str) == 2:
        return num_str[0] != num_str[1]

    if len(set(num_str)) == 1:
        return False

    for len_i in range(2, (len(num_str) + 1) // 2 + 1):
        if len(num_str) % len_i == 0:
            base_str = num_str[:len_i]
            for i in range(1, (len(num_str) // len_i)):
                if base_str == num_str[len_i * i : len_i * (i + 1)]:
                    continue
                break
            else:
                return False

    return True


def get_input() -> list[tuple[int, int]]:
    ranges = list()

    with open(FILENAME) as file:
        line = file.readline().strip()
        for range_str in line.split(","):
            num1, num2 = map(int, range_str.split("-"))
            ranges.append((num1, num2))

    return ranges


def part_1():
    ranges = get_input()
    result = 0

    for r1, r2 in ranges:
        for n in range(r1, r2 + 1):
            if not is_valid1(n):
                result += n

    print(f"Answer is {result}")


def part_2():
    ranges = get_input()
    result = 0

    for r1, r2 in ranges:
        for n in range(r1, r2 + 1):
            if not is_valid2(n):
                result += n

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
