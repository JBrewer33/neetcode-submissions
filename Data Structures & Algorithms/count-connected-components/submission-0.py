class Solution:


    def bfs(self, visited, graph, start):
        queue = deque()
        queue.append(start)
        visited.add(start)
        while queue:
            curr = queue.popleft()

            for node in graph[curr]:
                if node not in visited:
                    queue.append(node)
                    visited.add(node)




    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        comps = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                comps += 1
                self.bfs(visited, graph, i)

        return comps