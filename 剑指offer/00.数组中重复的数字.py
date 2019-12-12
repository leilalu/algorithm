"""
找出数组中重复的数字。
在一个长度为n的数组里的所有数字都在0～n-1的范围。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

例如：
如果输入长度为7的数组[2,3,1,0,2,5,3],那么对应的输出是重复的数字2或3

"""


class Solution:
    def find_duplicate_1(self, nums):
        """
        先对输入数组进行排序，然后从头到尾扫描排序后的数组，找到与前一个相同的元素就是重复元素
        排序一个长度为n的数组需要 O(nlogn) 的时间

        :param nums:
        :return:
        """
        if not nums or len(nums) == 0 or len(nums) == 1:
            return
        nums = sorted(nums)  # python中对数组排序的内置函数，默认升序
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def find_duplicate_2(self, nums):
        """
        借助哈希表实现。
        从头到尾按顺序扫描数组的每个数字，每扫描到一个数字的时候，都可以用 O(1) 的时间来判断哈希表里是否已经包含了该数字。
        如果哈希表里已经存在该数字，就找到一个重复数字。
        这个算法的时间复杂度是 O(n)，但是它提高时间效率是以一个大小为 O(n) 的哈希表为代价的。

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

    def find_duplicate_3(self, nums):
        """
        注意输入数组的条件：长度为n， 所有数字都在0～n-1的范围
        因此如果数组中没有重复的数字，那么数组的索引i应该和数组的数字i相等

        :param nums:
        :return:
        """
        if not nums or len(nums) <= 0 or len(nums) == 1:
            return

        for i in range(len(nums)):
            # 判断所有数字在0～n-1的范围之间
            if nums[i] < 0 or nums[i] > (len(nums) - 1):
                return

        for i in range(len(nums)):

            while nums[i] != i:
                if nums[i] == nums[nums[i]]:
                    return nums[i]

                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    res = s.find_duplicate_3(nums)
    print(res)
