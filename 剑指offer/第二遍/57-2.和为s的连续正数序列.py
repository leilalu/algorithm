"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

"""


class Solution:
    def findContinuousSequence(self, target):
        if target < 3:
            return []

        small = 1
        big = 2
        middle = (target + 1) // 2
        curSum = small + big

        result = []

        while small < middle:
            if curSum == target:
                sequence = self.PrintSequence(small, big)
                result.append(sequence)

            while curSum > target and small < middle:
                curSum -= small
                small += 1

                if curSum == target:
                    sequence = self.PrintSequence(small, big)
                    result.append(sequence)

            big += 1
            curSum += big

        return result

    def PrintSequence(self, small, big):
        sequence = []
        for i in range(small, big+1):
            sequence.append(i)
        return sequence






