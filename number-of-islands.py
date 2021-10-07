# https://leetcode.com/problems/number-of-islands/



def numIslands(grid):
    m = len(grid)
    n = len(grid[0])
    def mapIsland(i,j, visit):
        print(i, j)
        if i + 1 in range(m) and grid[i+1][j] == str(1) and visit[i+1][j] == 0:   # Check bottom
            visit[i+1][j] = 1
            mapIsland(i+1, j, visit)
        if j + 1 in range(n) and grid[i][j+1] == str(1) and visit[i][j+1] == 0:   # Check right
            visit[i][j+1] = 1
            mapIsland(i,  j+1, visit)
        if i - 1 in range(m) and grid[i-1][j] == str(1) and visit[i-1][j] == 0:   # Check top
            visit[i-1][j] = 1
            mapIsland(i-1, j, visit)
        if j - 1 in range(n) and grid[i][j-1] == str(1) and visit[i][j-1] == 0:   # Check left
            visit[i][j-1] = 1
            mapIsland(i, j-1, visit)
        
            
    import numpy as np
    
    copied_grid = np.zeros((m, n))
    islandCount = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == str(1) and copied_grid[i][j] == 0:
                copied_grid[i][j] = 1
                islandCount += 1
                mapIsland(i,j, copied_grid)
                print(copied_grid)
    return islandCount

test = [["0","1","0"],["1","0","1"],["0","1","0"]]

print(numIslands(test))