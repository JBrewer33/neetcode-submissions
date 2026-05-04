class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted(nums)
        n = Counter(nums)
        return [key[0] for key in n.most_common(k)]
        