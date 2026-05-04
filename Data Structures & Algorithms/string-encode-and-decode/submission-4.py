class Solution:

    def encode(self, strs: List[str]) -> str:
        build = ""
        for s in strs:
            build += str(len(s)) + '#' + s
        return build

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            itr = s.find('#', i)
            l = int(s[i:itr])
            itr += 1
            strs.append(s[itr:itr+l])
            i = itr+l
        return strs
