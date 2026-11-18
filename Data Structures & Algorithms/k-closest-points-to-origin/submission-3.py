class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #k closest == max heap of distances of size k
        #create heap
        #for each point calc euclidian distance add to heap if smaller than top, if heap goes above size k, pop top

        max_heap = []

        for point in points:
            dist = math.sqrt( (point[0] ** 2) + (point[1] ** 2) )
            print(str(dist))
            if len(max_heap) < k or dist < max_heap[0][0]:
                
                heapq.heappush_max(max_heap, (dist, point))
                if len(max_heap) > k:
                    heapq.heappop_max(max_heap)
        ret = []
        for point in max_heap:
            ret.append(point[1])

        return ret
