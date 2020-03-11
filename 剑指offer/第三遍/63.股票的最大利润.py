class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) <= 0:
            return 0

        minPrice = prices[0]
        curDiff = 0
        maxDiff = 0

        for i in range(1, len(prices)):
            # 更新 前 i-1 个价格的最小值
            if prices[i-1] < minPrice:
                minPrice = prices[i-1]

            curDiff = prices[i] - minPrice

            if curDiff > maxDiff:
                maxDiff = curDiff

        return maxDiff