class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*m for _ in range(n)]
        for ys in grid:
            ys[0] = 1

        grid[0] = [1]*m

        for y in range(1, m):
            for x in range(1,n):
                grid[x][y] = grid[x][y-1] + grid[x-1][y]

        return grid[n-1][m-1]





        