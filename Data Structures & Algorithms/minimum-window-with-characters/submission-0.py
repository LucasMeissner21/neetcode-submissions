class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        window = {}
        freqT = {}

        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)

        have, need = 0, len(freqT)

        res = ""
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if freqT.get(c, 0) == window[c]:
                have += 1

            while have == need:
                curr = s[l:r + 1]
                if len(curr) < len(res) or res == "":
                    res = curr
                
                window[s[l]] -= 1
                if freqT.get(s[l], 0) > window[s[l]]:
                    have -= 1
                
                l += 1
        return res
            