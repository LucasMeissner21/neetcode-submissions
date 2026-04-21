class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ",".join(str(len(s)) for s in strs)
        res += '#'
        res += "".join(strs)
        return res
        
        
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        i = 0
        while s[i] != '#':
            i += 1
        lensub = s[0:i]
        lengths = lensub.split(',')
        i += 1
        for l in lengths:
            length = int(l)
            res.append(s[i:i+length])
            i += length
        return res