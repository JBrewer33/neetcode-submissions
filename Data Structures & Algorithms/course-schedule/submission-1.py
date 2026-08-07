class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses

        adj = [[] for i in range(numCourses)]

        for source, dest in prerequisites:
            indegree[dest] += 1
            adj[source].append(dest)

        queue = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        finish = 0

        while queue:
            node = queue.popleft()
            finish += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            
        return finish == numCourses