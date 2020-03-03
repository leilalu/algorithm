"""
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序


输入一个正数s，打印出所有和为s的连续正数序列（至少含有两个数）
例如，输入15，由于1+2+3+4+5 = 4+5+6 = 7+8 = 15
所以打印出3个连续序列1～5，4～6，7～8

"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # 序列至少要有两个正数，最小的两个正数是1，2。如果和小于3，则没有连续的正数序列的和为小于3的数
        if tsum < 3:
            return []

        small = 1
        big = 2
        middle = (tsum+1) // 2
        curSum = small + big

        res = []

        while small < middle:
            if curSum == tsum:
                sequence = self.PrintContinuousSequence(small, big)
                res.append(sequence)

            while curSum > tsum and small < middle:
                curSum -= small
                small += 1

                if curSum == tsum:
                    sequence = self.PrintContinuousSequence(small, big)
                    res.append(sequence)

            big += 1
            curSum += big

        return res

    def PrintContinuousSequence(self, small, big):
        sequence = []
        for i in range(small, big+1):
            sequence.append(i)
        return sequence


if __name__ == '__main__':
    tsum = 9
    s = Solution()
    res = s.FindContinuousSequence(tsum)
    print(res)


