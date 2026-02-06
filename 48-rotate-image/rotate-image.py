class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)

        done = set()
        for j in range(size):
            for i in range(j,size):
                # if f"{i}-{j}" in done:
                #     continue
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                done.add(f"{i}-{j}")
                done.add(f"{j}-{i}")

        for j in range(size):
            for i in range(size):
                if i <= size//2 - 1:
                    matrix[j][i], matrix[j][size-1-i] = matrix[j][size-1-i], matrix[j][i]


        