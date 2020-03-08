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
            从头到尾遍历数组中的数字，并且记录到目前为止的之前数字的累加和和最大的累加和

            当之前数字的累加和是个负数时，加上当前数字，累加和一定会比当前数字还小，因此将累加和更新为当前数字
            当累加和是个正数时，无论当前数字是什么，都可以相加计算累加和

            每次计算完当前数字的累加和后，要计算当前数字最大的累加和，如果比最大还大，才更新最大累加和

        """
        # 检查无效输入，数组为空时累加和为0
        if not array or len(array) <= 0:
            return 0

        curSum = array[0]
        maxSum = array[0]

        for i in range(1, len(nums)):
            if curSum <= 0:
                curSum = nums[i]
            else:
                curSum += nums[i]

            if curSum > maxSum:
                maxSum = curSum

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



if __name__ == '__main__':
    nums = [8, -19, 5, -4, 20]
    res = Solution1().FindGreatestSumOfSubArray(nums)
    print(res)



















