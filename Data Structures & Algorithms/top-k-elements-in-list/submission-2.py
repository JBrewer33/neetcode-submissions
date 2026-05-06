class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums).most_common(k)
        ret = []
        for count in counts:
            ret.append(count[0])
        return ret