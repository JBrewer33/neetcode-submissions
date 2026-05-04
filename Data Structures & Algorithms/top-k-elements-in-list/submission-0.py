class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2:
            return nums
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        topk = heapq.nlargest(k, count.keys(), key=count.get)
        return topk        
            