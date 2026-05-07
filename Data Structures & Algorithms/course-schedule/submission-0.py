#graph where [a,b] represents a directed edge from b to a
#we need to determine if we can start at a node n and move to numCourses distict nodes without hitting a cycle
#dfs or khans for cycle detection


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = [[] for i in range(numCourses)]
        for source, destination in prerequisites:
            graph[source].append(destination)
            indegree[destination] += 1
        
        queue = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        count = 0
        while queue:
            current = queue.popleft()
            count += 1
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return count == numCourses