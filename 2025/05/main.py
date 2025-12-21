FILENAME = "input.txt"


def get_input() -> tuple[list[tuple[int, int]], list[int]]:
    fresh_ranges = list()
    ingredient_IDs = list()

    range_flag = True

    with open(FILENAME) as file:
        for line in file.readlines():
            line = line.strip()

            if line == "":
                range_flag = False
                continue

            if range_flag:
                fresh_ranges.append(tuple(map(int, line.split("-"))))

            else:
                ingredient_IDs.append(int(line))

    return fresh_ranges, ingredient_IDs


def part_1():
    fresh_ranges, ingredient_IDs = get_input()
    result = 0

    for curr_ID in ingredient_IDs:
        for min_r, max_r in fresh_ranges:
            if min_r <= curr_ID <= max_r:
                result += 1
                break

    print(f"Answer is {result}")


def part_2():
    fresh_ranges, ingredient_IDs = get_input()
    result = 0

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
