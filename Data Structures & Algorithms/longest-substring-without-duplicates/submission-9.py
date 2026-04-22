class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window with hashmap
        
        mp = {} # key = character, value = index
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l) # max accounts for l staying past previous values, map not set
            mp[s[r]] = r
            res = max(res, r-l+1)
        return res