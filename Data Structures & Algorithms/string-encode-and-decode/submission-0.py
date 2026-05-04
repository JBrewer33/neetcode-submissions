class Solution:

    def encode(self, strs: List[str]) -> str:
        build = ""
        for s in strs:
            build += str(len(s)) + '#' + s
        return build

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0 #pointer to find delimiter character
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            content = s[j + 1 : j + 1 + length]
            strs.append(content)
            i = j + 1 + length
        return strs
