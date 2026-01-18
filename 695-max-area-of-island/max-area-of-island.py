class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        visited = set()

        def find_area(j, i):
            if j<0 or j>=height:
                return 0
            if i < 0 or i>=width:
                return 0
            if grid[j][i] == 0:
                return 0
            grid[j][i] = 0 
            return 1 + find_area(j+1, i) +find_area(j-1, i)+find_area(j, i-1)+find_area(j, i+1)

        max_area = 0
        for j in range(0, height):
            for i in range(0, width):
                if grid[j][i] != 0:
                    max_area = max(max_area, find_area(j, i))

        return max_area

                    
        