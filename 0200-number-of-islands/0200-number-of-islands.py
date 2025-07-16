class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island = 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            if not (0 <= r < rows and 0 <= c <cols): return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                dfs(r+dr, c+dc)

            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] =='1':
                    island += 1
                    dfs(r, c)
        return island