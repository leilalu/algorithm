class Solution:
    def maxSubArray(self, nums):
        # 检查无效输入
        if not nums or len(nums) <= 0:
            return None

        curSum = 0
        maxSum = nums[0]  # 一定要让最大值为数组中的数
        for i in range(len(nums)):
            if curSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]

            if curSum > maxSum:
                maxSum = curSum

        return maxSum


class Solution1:
    def maxSubArray(self, nums):
        if not nums or len(nums) <= 0:
            return None

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]

        print(dp)
        maxSum = nums[0]
        for i in range(len(nums)):
            if dp[i] > maxSum:
                maxSum = dp[i]
        return maxSum


if __name__ == '__main__':
    nums = [-2]
    res = Solution1().maxSubArray(nums)
    print(res)

