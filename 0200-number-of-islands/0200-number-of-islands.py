class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        island =0

        def bfs(start_row, start_col):
            queue = deque()
            queue.append((start_row, start_col))
            grid[start_row][start_col]='0'

            directions =[(-1,0),(1,0),(0,-1),(0,1)]
            while queue:
                row, col = queue.popleft()
                for d_row, d_col in directions:
                    new_row = row + d_row
                    new_col = col+d_col
            #유효하고 땅이면
                    if (
                        0 <= new_row <rows and
                        0 <= new_col <cols and 
                        grid[new_row][new_col] == '1'
                    ):
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = '0'
            #전체 grid 돌면서 bfs 시작 지점 찾기
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island += 1
                    bfs(r,c)
                
        return island