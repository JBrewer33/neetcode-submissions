class Solution:

    def bfs(self, i, j, grid):
        queue = deque()
        grid[i][j] = "0"
        queue.append((i, j))

        while queue:
            curr = queue.pop()
            rightBound = len(grid) - 1
            downBound = len(grid[0]) - 1

            if curr[0] < rightBound and grid[curr[0]+1][curr[1]] == "1":
                grid[curr[0]+1][curr[1]] = "0"
                queue.append((curr[0]+1, curr[1]))

            if curr[1] < downBound and grid[curr[0]][curr[1]+1] == "1":
                grid[curr[0]][curr[1]+1] = "0"
                queue.append((curr[0], curr[1]+1))

            if curr[0] > 0 and grid[curr[0]-1][curr[1]] == "1":
                grid[curr[0]-1][curr[1]] = "0"
                queue.append((curr[0]-1, curr[1]))

            if curr[1] > 0 and grid[curr[0]][curr[1]-1] == "1":
                grid[curr[0]][curr[1]-1] = "0"
                queue.append((curr[0], curr[1]-1))
            

    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0

        #iterate whole grid, when hit island, count and bfs to clear island (flip 1 to 0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(i, j, grid)
                    count += 1
        
        return count