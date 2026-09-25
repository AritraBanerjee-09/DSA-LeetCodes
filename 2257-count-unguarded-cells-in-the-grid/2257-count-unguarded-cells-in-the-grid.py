class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        grid = [[0]* n for _ in range(m)] #matrix

        #place guards
        for r, c in guards:
            grid[r][c] = 1

        #place walls
        for r, c in walls:
            grid[r][c] = 2
        
        #check every guard
        for r,c in guards:
            #up
            i = r-1
            while i>= 0:
                if grid[i][c] == 1 or grid[i][c] == 2:
                    break
                grid[i][c] = 3
                i -= 1
            
            #down
            i = r + 1
            while i < m:
                if grid[i][c] == 1 or grid[i][c] == 2:
                    break
                grid[i][c] = 3
                i += 1

            # LEFT
            j = c - 1
            while j >= 0:
                if grid[r][j] == 1 or grid[r][j] == 2:
                    break
                grid[r][j] = 3
                j -= 1

            # RIGHT
            j = c + 1
            while j < n:
                if grid[r][j] == 1 or grid[r][j] == 2:
                    break
                grid[r][j] = 3
                j += 1

        # Count unguarded empty cells
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    count += 1

        return count