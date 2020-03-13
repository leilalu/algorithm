"""

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

"""
import random


class Solution:
    def majorityElement(self, nums):
        length = len(nums)
        if not nums or length <= 0:
            return None

        # if length == 1:
        #     return nums[0]

        # 计算开头、中间、结尾
        middle = length >> 1
        start = 0
        end = length - 1

        # 快排划分索引
        index = self.Partition(nums, start, end)

        while index != middle:
            if index > middle:
                end = index - 1
                index = self.Partition(nums, start, end)
            else:
                start = index + 1
                index = self.Partition(nums, start, end)

        result = nums[middle]
        if not self.Check(nums, length, result):
            return 0
        return result

    def Partition(self, nums, start, end):
        # 找到随机划分点
        if start == end:
            pivot = start
        else:
            pivot = random.randrange(start, end)

        # 将随机划分点放在最后
        nums[pivot], nums[end] = nums[end], nums[pivot]

        # 设置分区点，0～i-1的元素都是小于pivot的，i～end-1的元素都是大于pivot的
        # 因此当nums[j]小于pivot时，应该将其与nums[i]交换，相当于将nums[j]填在了nums[i-1]之后，i向后移一位
        # 最后nums[i] 应该与nums[end]即pivot交换，意味着将pivot填到nums[i-1]之后，此时i就是pivot的下标了
        i = start
        for j in range(start, end):
            if nums[j] < nums[end]:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[end], nums[i] = nums[i], nums[end]

        return i

    def Check(self, nums, length, number):
        """"
        检查某一个数字是否出现了超过半数次

        """
        times = 0
        for i in range(length):
            if nums[i] == number:
                times += 1
        if times * 2 > length:
            return True
        return False


if __name__ == '__main__':
    nums = [2]
    res = Solution().majorityElement(nums)
    print(res)

