class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        if len(strs) == 0:
            return []
        for word in strs:
            key = "".join(sorted(word))
            if key in out:
                out[key].append(word)
            else:
                out[key] = [word]
        return list(out.values())