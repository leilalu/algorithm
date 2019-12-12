"""
不修改数组找出重复的数字
在一个长度为 n+1 的数组里的所有数字都在 1~n 的范围内，所有数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组。

例如：
如果输入长度为8的数组[2,3,5,4,3,2,6,7]
那么应该对应的输出是重复的数字2或3

Note: 当给出数组的长度和数字的取值范围时，一定要从数组的索引和数字的关系入手。

"""


class Solution:
    def find_duplicate(self, nums):
        """
        借助辅助哈希表

        :param nums:
        :return:
        """
        if not nums or len(nums) == 0 or len(nums) == 1:
            return
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)
            else:
                return num


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,5,4,3,2,6,7]
    res = s.find_duplicate(nums)
    print(res)