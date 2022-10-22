grid = []
for _ in range(4):
    grid.append(list(input()))

print(grid[0][0])


def dfs(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        return

    grid[i][j] = 0

    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)


count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '1':
            dfs(i, j)
            count += 1

print(count)
