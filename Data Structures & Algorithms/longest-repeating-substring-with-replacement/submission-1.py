class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window with hashmap
        count = defaultdict(int) # key = char, val = freq

        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            # Update frequency and highest seen frequency
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            # If window - highest seen frequency > num replacements, shorten window
            while r - l + 1 - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
            