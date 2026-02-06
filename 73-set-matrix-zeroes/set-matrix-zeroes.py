class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cordinates = set()
        zero_rows = set()
        zero_cols = set()

        y = len(matrix)
        x = len(matrix[0])

        for j in range(y):
            for i in range(x):
                if matrix[j][i] == 0:
                    zero_rows.add(j)
                    zero_cols.add(i)
        
        for j in range(y):
            if j in zero_rows:
                matrix[j] = [0]*x
            for i in range(x):
                if i in zero_cols:
                    matrix[j][i] = 0
        