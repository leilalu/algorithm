"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

 

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1:

输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2
 

限制：

1 <= 数组长度 <= 50000


"""

import random


class Solution:
    def majorityElement(self, nums):
        length = len(nums)
        # 非法输入检查
        if not nums or length <= 0:
            return 0

        # 数组中只有一个月元素
        if length == 1:
            return nums[0]

        # 计算起始、终止、中间位置
        middle = length >> 1
        start = 0
        end = length - 1

        # Partition函数划分的索引
        index = self.Partition(nums, start, end)

        while index != middle:
            if index > middle:
                end = index - 1
                index = self.Partition(nums, start, end)
            else:
                start = index + 1
                index = self.Partition(nums, start, end)

        result = nums[middle]
        if not self.CheckMoreThanHalf(nums, length, result):
            # 说明该数组中不存在出现次数超过半数的
            return 0
        return result

    def Partition(self, nums, start, end):
        # 随机找到一个划分点
        if start == end:
            pivot = start
        else:
            pivot = random.randrange(start, end)

        # 把这个划分点的值放在最后一位上
        nums[pivot], nums[end] = nums[end], nums[pivot]

        # 记录比所选数小的数
        small = start - 1
        for i in range(start, end):
            if nums[i] < nums[end]:
                small += 1
                if small != i:
                    # 此时small指向的是第一个大于pivot的数,大数和小数调换
                    nums[small], nums[i] = nums[i], nums[small]
        small += 1
        nums[small], nums[end] = nums[end], nums[pivot]

        return small

    def CheckMoreThanHalf(self, nums, length, number):
        """"
        检查某一个数字是否出现了超过半数次

        """
        times = 0
        for i in range(length):
            if nums[i] == number:
                times += 1
        if times * 2 <= length:
            return False
        return True


if __name__ == '__main__':
    nums = [-1,100,2,100,100,4,100]
    res = Solution().majorityElement(nums)
    print(res)





