"""
题目：

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

例如，一只股票在某些时间节点的价格为[9,11,8,5,7,12,16,14].
如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。

"""


class Solution:
    def MaxDiff(self, numbers):
        if not numbers or len(numbers) < 2:
            return 0

        min = numbers[0]  # 前 i-1 时刻的最低佳
        maxDiff = numbers[1] - min

        for i in range(2, len(numbers)):
            # 如果价格比之前最小的价格还低。卖出价一定，买入价越低越好
            if numbers[i-1] < min:
                min = numbers[i-1]

            curDiff = numbers[i] - min
            if curDiff > maxDiff:
                maxDiff = curDiff

        return maxDiff