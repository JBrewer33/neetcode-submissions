#first thoughts, since we need to search a grid, will likely be bfs/dfs
#strategy - iterate arrays top left to bottom right, when we hit an island increment count, launch bfs from there mark all visted
#return, continue
#when we get to bottom left all island points will be visted and counted
#for dfs want to use the existing grid for visted for simplicity and space, if need to preserve original, create
#visited array to update as we go adds extra space


class Solution:
	def bfsIsland(self, grid: List[List[int]], start: Tuple(int, int)) -> None:
		queue = deque()
		
		grid[start[0]][start[1]] = "2" #mark visited
		queue.append(start)
		
		while queue:
			current = queue.popleft()
			i = current[0]
			j = current[1]
			
			#4 directions, each needs bounds check and land check
			if i > 0 and grid[i-1][j] == "1":
				grid[i-1][j] = "2"
				queue.append((i-1, j))
			if j > 0 and grid[i][j-1] == "1":
				grid[i][j-1] = "2"
				queue.append((i, j-1))
			if i < len(grid) - 1 and grid[i+1][j] == "1":
				grid[i+1][j] = "2"
				queue.append((i+1, j))
			if j < len(grid[0]) - 1 and grid[i][j+1] == "1":
				grid[i][j+1] = "2"
				queue.append((i, j+1))
		#no need for return value when function is done all parts of island will be marked visted
		
	def numIslands(self, grid: List[List[str]]) -> int:
		
		count = 0
		
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == "1":
					count += 1 
					self.bfsIsland(grid, (i, j))
		
		return count
		
#Time - iterate full grid all ops O(1) = O(n + m)
#Space - modifying grid in place, worst case queue == n so = O(n) 