class Solution:

    def bfs(self, start, grid):
        queue = deque()
        queue.append(start)
        grid[start[0]][start[1]] = "0"
        while queue:
            curr = queue.popleft()
            i = curr[0]
            j = curr[1]
            if i + 1 < len(grid) and grid[i+1][j] == "1":
                queue.append((i+1, j))
                grid[i+1][j] = "0"
            if j + 1 < len(grid[0]) and grid[i][j+1] == "1":
                queue.append((i, j+1))
                grid[i][j+1] = "0"
            if i - 1 > -1 and grid[i-1][j] == "1":
                queue.append((i-1, j))
                grid[i-1][j] = "0"
            if j - 1 > -1 and grid[i][j-1] == "1":
                queue.append((i, j-1))
                grid[i][j-1] = "0"





    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs((i, j), grid)
                    count += 1
        
        return count
