class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case, no permutations can exist
        if len(t) > len(s):
            return ""

        # Hashmap for the window and freq
        window = {}
        freqT = {}

        # Initialize freqT
        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)

        # Check unique characters in t, set to matches needed
        have, need = 0, len(freqT)

        res = ""
        l = 0
        for r in range(len(s)):
            # Slide window and adjust frequency
            c = s[r]
            window[c] = 1 + window.get(c,0)

            # Check if new window has character requirements for permutation for c
            if freqT.get(c, 0) == window[c]:
                have += 1

            # Once all needs are met, adjusts res if current is smaller and shrinks window until no longer a match
            while have == need:
                curr = s[l:r + 1]
                if len(curr) < len(res) or res == "":
                    res = curr
                
                window[s[l]] -= 1
                if freqT.get(s[l], 0) > window[s[l]]:
                    have -= 1
                
                l += 1
        return res
            