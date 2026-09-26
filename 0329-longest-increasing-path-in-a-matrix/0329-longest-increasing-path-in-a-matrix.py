class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, col = len(matrix), len(matrix[0])
        # hashmap
        dp = {}

        def dfs(r, c, pr):
            if(r<0 or r == rows or
                c<0 or c == col or
                matrix[r][c] <= pr):
                return 0
            
            if (r, c) in dp:
                return dp[(r,c)]
            
            res = 1
            res = max(res, 1+ dfs(r+1 , c, matrix[r][c]))
            res = max(res, 1+ dfs(r-1 , c, matrix[r][c]))
            res = max(res, 1+ dfs(r , c+1, matrix[r][c]))
            res = max(res, 1+ dfs(r , c-1, matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        for r in range(rows):
            for c in range(col):
                dfs(r,c, -1)
        return max(dp.values())