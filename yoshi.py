# X = ON
# O = OFF

# Line 1: Grid length (l)
# Line 2: Amount of moves (m)
# l lines of X and O (Initial state)
#
# l lines of X and O (Goal state)
#
# Example:
# XOXX
# OXOO
# XOOX
# OXOX

from itertools import product

l = int(input().strip())
m = int(input().strip())
initial_state = [input().strip() for _ in range(l)]
goal_state = [input().strip() for _ in range(l)]

def toggle(grid, x, y):
    # Toggle (x, y) and all 8 neighbors
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l:
                grid[nx][ny] = 'O' if grid[nx][ny] == 'X' else 'X'

def grid_to_list(grid):
    return [list(row) for row in grid]

def list_to_grid(grid):
    return [''.join(row) for row in grid]

def solve():
    positions = [(i, j) for i in range(l) for j in range(l)]
    for moves in product(positions, repeat=m):
        grid = grid_to_list(initial_state)
        for x, y in moves:
            toggle(grid, x, y)
        if list_to_grid(grid) == goal_state:
            # Print moves as 0-indexed, column first then row
            for x, y in moves:
                print(f"{y} {x}")
            return
    print("No solution found")

solve()

