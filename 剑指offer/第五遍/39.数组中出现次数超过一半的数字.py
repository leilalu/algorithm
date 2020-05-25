"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。


示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

"""
import random


class Solution1:
    def majorityElement(self, nums):
        if not nums or len(nums) <= 0:
            return None

        left = 0
        right = len(nums) - 1
        mid = left + ((right - left) >> 1)

        pivot = self.Partition(nums, left, right)

        while pivot != mid:
            if pivot > mid:
                right = pivot - 1
                pivot = self.Partition(nums, left, right)
            else:
                left = pivot + 1
                pivot = self.Partition(nums, left, right)

        res = nums[pivot]

        if not self.check(nums, res):
            return None

        return nums[pivot]

    def Partition(self, nums, start, end):
        if start == end:
            pivot = start
        else:
            pivot = random.randrange(start, end)

        nums[pivot], nums[end] = nums[end], nums[pivot]

        i = start
        for j in range(start, end):
            if nums[j] < nums[end]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[end] = nums[end], nums[i]

        return i

    def check(self, nums, res):
        count = 0
        for num in nums:
            if num == res:
                count += 1
        if count * 2 > len(nums):
            return True
        return False


"""
采用投票法，时间复杂度为O(n)，而且不改变输入数组
基于Partition函数会修改输入数组

"""


class Solution2:
    def majorityElement(self, nums):
        if not nums or len(nums) <= 0:
            return None

        result = nums[0]  # 保存数字
        times = 1

        for i in range(1, len(nums)):
            if nums[i] == result:
                times += 1
            elif times == 0:
                result = nums[i]
                times = 1
            else:
                times -= 1

        if not self.check(nums, result):
            return None

        return result

    def check(self, nums, res):
        count = 0
        for num in nums:
            if num == res:
                count += 1
        if count * 2 > len(nums):
            return True
        return False


if __name__ == '__main__':
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    res = Solution2().majorityElement(nums)
    print(res)

