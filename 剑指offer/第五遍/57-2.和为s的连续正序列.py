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
        # 首先判断输入是否合法
        if target < 1:
            return []
        res = []

        small = 1
        big = small + 1
        curSum = 3

        while big <= target // 2 + 1:
            if curSum < target:
                big += 1
                curSum += big
            elif curSum > target:
                curSum -= small
                small += 1
            else:
                seq = [num for num in range(small, big+1)]
                res.append(seq)
                big += 1
                curSum += big

        return res


if __name__ == '__main__':
    target = 15
    res = Solution().findContinuousSequence(target)
    print(res)

