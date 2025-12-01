FILENAME = "input.txt"


def get_input() -> list[int]:
    integer_list = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            if line[0] == "L":
                integer_list.append(-int(line[1:]))
            else:
                integer_list.append(int(line[1:]))

    return integer_list


def part_1():
    rotations = get_input()
    current_position = 50
    result = 0

    for n in rotations:
        current_position += n
        current_position %= 100

        if current_position == 0:
            result += 1

    print(f"Answer is {result}")


def part_2():
    rotations = get_input()
    current_position = 50
    result = 0

    for n in rotations:
        if n < 0:
            if current_position != 0 and current_position + n <= 0:
                result += 1

            current_position += n

            if current_position <= 0:
                result += -current_position // 100

        else:
            current_position += n
            if current_position >= 100:
                result += current_position // 100

        current_position %= 100

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
