class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def dfs(r ,c ):
            if r>=m or r<0 or c>=n or c<0:
                return False
            
            if grid[r][c] == 1:
                return True
            
            grid[r][c] =  1

            left_close = dfs(r, c-1)
            right_close = dfs(r,c+1)
            up_close = dfs(r-1 ,c )
            down_close = dfs(r+1, c)

            return left_close and right_close  and up_close and down_close
        count =0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if dfs(i,j):
                        count += 1
        return count