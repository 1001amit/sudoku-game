import numpy as np
import random

def is_valid(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num or grid[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    return True

def fill_grid(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                random_nums = list(range(1, 10))
                random.shuffle(random_nums)
                for num in random_nums:
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if fill_grid(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True

def generate_complete_grid():
    grid = np.zeros((9, 9), dtype=int)
    fill_grid(grid)
    return grid

def create_puzzle(grid, difficulty='easy'):
    if difficulty == 'easy':
        attempts = 5
    elif difficulty == 'medium':
        attempts = 10
    else:  # 'hard'
        attempts = 15

    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while grid[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        
        backup = grid[row][col]
        grid[row][col] = 0
        
        grid_copy = grid.copy()
        if not solve(grid_copy):
            grid[row][col] = backup
            attempts -= 1

    return grid

