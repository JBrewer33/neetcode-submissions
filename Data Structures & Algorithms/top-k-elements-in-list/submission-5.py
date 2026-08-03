class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #frequency -- count map
        #top k -- min heap

        frequencyMap = Counter(nums)
        kLargest = heapq.nlargest(k, frequencyMap.items(), key=lambda x: x[1])

        ret = []

        for element in kLargest:
            ret.append(element[0])

        return ret