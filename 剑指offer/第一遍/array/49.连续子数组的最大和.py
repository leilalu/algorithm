"""
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

"""


class Solution1:
    def FindGreatestSumOfSubArray(self, array):
        """
        [-2,-8,-1,-5,-9]

        """
        # 检查无效输入
        if not array or len(array) <= 0:
            return 0

        curSum = array[0]
        maxSum = array[0]
        for num in array[1:]:
            if num > (curSum + num) and maxSum < num:
                curSum = num
                maxSum = num
            elif curSum + num > maxSum:
                maxSum = curSum + num
                curSum += num
            else:
                curSum += num

        return maxSum


class Solution2:
    def FindGreatestSumOfSubArray(self, array):
        """"
        动态规划：
            设f(i) 为第i个数字结尾的子数组的最大和，要返回max[f(i)]

            f(i) = array[i] (i=0, 或者 f(i-1) <= 0)
                   f(i-1) + array[i] (i 不等于0 且 f(i-1) > 0)

        """
        if not array:
            return 0
        # f(i) i=0
        dp = [array[0]]

        for i in range(1, len(array)):
            if dp[i-1] <= 0:
                dp.append(array[i])
            else:
                dp.append(dp[i-1] + array[i])

        return max(dp)






















