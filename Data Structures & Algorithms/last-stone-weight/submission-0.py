class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        heapq.heapify_max(stones)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop_max(maxHeap)
            stone2 = heapq.heappop_max(maxHeap)
            newStone = abs(stone1 - stone2)
            if newStone > 0:
                heapq.heappush_max(maxHeap, newStone)
        if len(maxHeap) == 0:
            return 0
        return maxHeap[0]