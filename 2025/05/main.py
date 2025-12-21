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
    fresh_ranges, __ = get_input()
    result = 0

    fresh_ranges.sort(key=lambda t: t[0])

    merged_ranges = [fresh_ranges.pop(0)]

    for rang in fresh_ranges:
        if merged_ranges[-1][1] < rang[0]:
            merged_ranges.append(rang)

        else:
            merged_ranges[-1] = (
                merged_ranges[-1][0],
                max(merged_ranges[-1][1], rang[1]),
            )

    for rang in merged_ranges:
        result += rang[1] - rang[0] + 1

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
