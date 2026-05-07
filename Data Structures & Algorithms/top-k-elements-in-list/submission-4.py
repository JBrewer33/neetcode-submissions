class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        countMap = defaultdict(int)

        for num in nums:
            countMap[num] += 1
            
        for num in countMap.keys():
            heapq.heappush(minHeap, (countMap[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
            

        return [num for _, num in minHeap]