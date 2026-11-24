class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size = len(p)
        ret = []
        comp = "".join(sorted(p))
        
        for i in range(len(s)):
            if i + size > len(s):
                break

            sub = s[i:i+size]
            sorted_sub = "".join(sorted(sub))
            print(sorted_sub)
            if sorted_sub == comp:
                ret.append(i)
        
        return ret