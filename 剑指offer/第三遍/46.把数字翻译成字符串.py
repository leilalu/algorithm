"""
给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，
11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"


"""


class Solution:
    def translateNum(self, num):
        if num < 0:
            return -1

        numString = str(num)

        return self.translateNumCore(numString)

    def translateNumCore(self, num):
        length = len(num)

        dp = [0] * length
        count = 0
        for i in range(length-1, -1, -1):
            if i < length-1:
                count = dp[i+1]
            else:
                count = 1

            if i < length-1:
                digit1 = int(num[i])
                digit2 = int(num[i+1])
                sumValue = digit1 * 10 + digit2
                if 10 <= sumValue <= 25:
                    if i < length - 2:
                        count += dp[i+2]
                    else:
                        count += 1
            dp[i] = count

        return dp[0]


if __name__ == '__main__':
    num = 12258
    res = Solution().translateNum(num)
    print(res)



