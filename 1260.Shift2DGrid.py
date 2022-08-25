# whhhhhhhhhhhhhhhhhhhy
def shiftGrid(grid, k)->list:
    m , n = len(grid), len(grid[0])
    def shiftOnce(grid):
        gridCopy = grid.copy()
        for i in range(m - 1):
            for j in range(n - 1):
                grid[i][j+1] = gridCopy[i][j]
            grid[i+1][0] = gridCopy[i][n-1]
        grid[0][0] = gridCopy[m - 1][n - 1]
        return grid
    for i in range(k):
        grid = shiftOnce(grid)
    return grid

grid = [[1,2,3],[4,5,6],[7,8,9]]
k = 1
print(shiftGrid(grid, k))