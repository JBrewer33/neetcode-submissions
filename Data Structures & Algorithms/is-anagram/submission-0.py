class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = sorted(s)
        ts = sorted(t)
        for i in range(len(s)):
            if ss[i] != ts[i]:
                return False
        return True