class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #initate array cooresponding to node number - 1 (for idx) to infi
        dist = [float('inf')] * n
        #set start node(k-1) dist to 0
        dist[k-1] = 0
        #for each edge u -> v if current distance to u (dist[u]) + time to v < distance to v (dist[v]) update dist[v] 
        for i in range(n-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
        #get maximum value in dist
        maxDist = 0
        for i in range(len(dist)):
            maxDist = max(maxDist, dist[i])
        #if inf mean disconnected return -1
        if maxDist == float('inf'):
            return -1
        return maxDist
        #else return value