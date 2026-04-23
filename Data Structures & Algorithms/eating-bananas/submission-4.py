class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Establish range for k, 1 to the largest pile size, and binary search based on if current k is possible.
        # If possible, adjust ub (r) to just before k. if takes too long, adjust lb (l) to just after k.
        r = max(piles)
        l = 1
        res = r

        while l <= r:
            k = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            if time <= h:
                res = k
                r = k - 1
            else:
                l = k + 1

        return res