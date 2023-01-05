class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        first, last = 0, 1
        prof = 0
        while last < len(prices):
            currentProfit = prices[last] - prices[first]
            if prices[first] < prices[last]:
                prof = max(currentProfit, prof)
            else:
                first = last
            last += 1
        return prof
