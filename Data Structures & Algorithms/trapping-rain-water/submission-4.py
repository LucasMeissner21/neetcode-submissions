class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointer approach
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        lmax = height[l]
        rmax = height[r]
        res = 0
        while l < r:
            # Max water height just depends on shorter wall height, so moving shorter wall adds water correctly
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                res += lmax - height[l]
            else:
                r -= 1
                rmax = max(rmax, height[r])
                res += rmax - height[r]
        return res