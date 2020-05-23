"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。

"""


class Solution:
    def exchange(self, nums):
        # 首先判断输入是否合法
        if not nums or len(nums) <= 0:
            return []

        left = 0
        right = len(nums) - 1

        while left < right:
            while left < right and nums[left] & 1 == 1:
                left += 1
            while left < right and nums[right] & 1 == 0:
                right -= 1

            nums[left], nums[right] = nums[right], nums[left]

            # 交换后不要忘记再往前走一步！！！
            left += 1
            right -= 1

        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    res = Solution().exchange(nums)
    print(res)


