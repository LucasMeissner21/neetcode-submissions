class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic approach
        maxP = 0
        minBuy = prices[0]

        for curPrice in prices:
            maxP = max(maxP, curPrice - minBuy)
            minBuy = min(minBuy, curPrice)

        return maxP