"""
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

示例1:

输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 

提示：

1 <= arr.length <= 10^5
-100 <= arr[i] <= 100

"""


class Solution1:
    def maxSubArray(self, nums):
        # 检查无效输入
        if not nums or len(nums) <= 0:
            return 0

        curSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            # 当当前累加和小于等于0时，就没必要再加新的数值只会比新的数值更小，所以累加和变为新的数值
            if curSum <= 0:
                curSum = nums[i]
            else:
                # 否则还是可以加新的数值
                curSum += nums[i]
            # 算晚当前累加和之后，判断当前最大累加和
            if curSum > maxSum:
                maxSum = curSum

        return maxSum


class Solution2:
    def maxSubArray(self, nums):
        if not nums or len(nums) <= 0:
            return 0

        dp = [nums[0]]

        for i in range(1, len(nums)):
            if dp[-1] <= 0:
                dp.append(nums[i])
            else:
                dp.append(nums[i] + dp[-1])

        return max(dp)


if __name__ == '__main__':
    nums = [8, -19, 5, -4, 20]
    res = Solution2().maxSubArray(nums)
    print(res)