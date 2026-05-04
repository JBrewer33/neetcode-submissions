class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            a = ''.join(sorted(s))
            seen[a].append(s)
        return list(seen.values())
        