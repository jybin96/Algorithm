T = int(input())


def dfs(grid, i, j):
    count = 0

    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return

    if grid[i][j] == '?':
        count += 1

    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)



for test_case in range(1, T + 1):
    i, j = map(int, input().split())
    grid = []
    for _ in range(i):
        row = [char for char in str(input())]
        grid.append(row)
    print(dfs(grid, 0, 0))

