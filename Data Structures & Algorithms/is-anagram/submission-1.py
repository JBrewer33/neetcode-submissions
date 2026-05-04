class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sl = sorted(s)
        tl = sorted(t)
        if sl == tl:
            return True
        return False