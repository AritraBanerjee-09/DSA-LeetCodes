class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        rt = [0 for _ in range(r)]
        ct = [0 for _ in range(c)]

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rt[i] = -1
                    ct[j] = -1
        
        for i in range(r):
            for j in range(c):
                if rt[i] == -1 or ct[j] == -1:
                    matrix[i][j] = 0

