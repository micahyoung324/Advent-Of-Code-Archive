from header import *


def count_adjacent_occupied(grid: list[list[str]], row: int, col: int) -> int:
    count = 0

    for x, y in DIRECTIONS:
        if 0 <= row + y < len(grid) and 0 <= col + x < len(grid[0]):
            if grid[row + y][col + x] == OCCUPIED:
                count += 1

    return count


def iterate_grid(grid: list[list[str]]) -> list[list[str]]:
    result = deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            adjacent_count = count_adjacent_occupied(grid, i, j)

            if grid[i][j] == EMPTY and adjacent_count == 0:
                result[i][j] = OCCUPIED

            elif grid[i][j] == OCCUPIED and adjacent_count >= 4:
                result[i][j] = EMPTY

    return result


def run_solution(grid_input: list[list[str]]):
    grid = deepcopy(grid_input)
    prev_grid = []
    count = 0

    while prev_grid != grid:
        prev_grid = deepcopy(grid)
        grid = iterate_grid(grid)

    for row in grid:
        for ch in row:
            if ch == OCCUPIED:
                count += 1

    print(f"There are {count} occupied seats.")
