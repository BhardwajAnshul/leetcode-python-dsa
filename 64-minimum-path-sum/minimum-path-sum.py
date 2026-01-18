# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:

#         leny = len(grid)
#         lenx = len(grid[0])
                
#         @lru_cache(None)
#         def total_cost(i, j):
#             if i== 0 and j == 0:
#                 return 0
#             elif i == 0:
#                 return total_cost(i, j-1) + grid[j-1][i]
#             elif j == 0:
#                 return total_cost(i-1, j) + grid[j][i-1]
#             else:
#                 return min(
#                     total_cost(i-1, j) + grid[j][i-1],
#                     total_cost(i, j-1) + grid[j-1][i]
#                 )

#         return total_cost(lenx-1, leny-1) + grid[leny-1][lenx-1]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]
