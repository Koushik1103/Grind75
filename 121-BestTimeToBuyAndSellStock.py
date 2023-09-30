class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        maxi = 0
        for i in prices[1:]:
            maxi = max(maxi, i - min_price)
            min_price = min(min_price, i)
        return maxi
