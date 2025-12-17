FILENAME = "input.txt"

PAPER = '@'
EMPTY = '.'


def get_input() -> list[list[str]]:
    paper_diagram = list()

    with open(FILENAME) as file:
        for line in file.readlines():
            paper_diagram.append(list(line.strip()))

    return paper_diagram


def part_1():
    paper_diagram = get_input()
    result = 0

    MAX_X = len(paper_diagram[0])
    MAX_Y = len(paper_diagram)

    for y in range(MAX_Y):
        for x in range(MAX_X):
            if paper_diagram[y][x] == EMPTY:
                continue

            count = 0

            if y > 0:
                if x > 0 and paper_diagram[y-1][x-1] == PAPER:
                    count += 1
                
                if paper_diagram[y-1][x] == PAPER:
                    count += 1

                if x < MAX_X - 1 and paper_diagram[y-1][x+1] == PAPER:
                    count += 1

            if y < MAX_Y - 1:
                if x > 0 and paper_diagram[y+1][x-1] == PAPER:
                    count += 1
                
                if paper_diagram[y+1][x] == PAPER:
                    count += 1

                if x < MAX_X - 1 and paper_diagram[y+1][x+1] == PAPER:
                    count += 1

            if x > 0 and paper_diagram[y][x-1] == PAPER:
                    count += 1

            if x < MAX_X - 1 and paper_diagram[y][x+1] == PAPER:
                    count += 1

            if count < 4:
                result += 1

    print(f"Answer is {result}")


def part_2():
    paper_diagram = get_input()
    result = 0

    MAX_X = len(paper_diagram[0])
    MAX_Y = len(paper_diagram)

    stop_flag = False

    while not stop_flag:
        stop_flag = True
        new_paper_diagram = [[ch for ch in row] for row in paper_diagram]

        for y in range(MAX_Y):
            for x in range(MAX_X):
                if paper_diagram[y][x] == EMPTY:
                    continue

                count = 0

                if y > 0:
                    if x > 0 and paper_diagram[y-1][x-1] == PAPER:
                        count += 1
                    
                    if paper_diagram[y-1][x] == PAPER:
                        count += 1

                    if x < MAX_X - 1 and paper_diagram[y-1][x+1] == PAPER:
                        count += 1

                if y < MAX_Y - 1:
                    if x > 0 and paper_diagram[y+1][x-1] == PAPER:
                        count += 1
                    
                    if paper_diagram[y+1][x] == PAPER:
                        count += 1

                    if x < MAX_X - 1 and paper_diagram[y+1][x+1] == PAPER:
                        count += 1

                if x > 0 and paper_diagram[y][x-1] == PAPER:
                        count += 1

                if x < MAX_X - 1 and paper_diagram[y][x+1] == PAPER:
                        count += 1

                if count < 4:
                    stop_flag = False
                    new_paper_diagram[y][x] = EMPTY
                    result += 1

        paper_diagram = new_paper_diagram

    print(f"Answer is {result}")


if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
