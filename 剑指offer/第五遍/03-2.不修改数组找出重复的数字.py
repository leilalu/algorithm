"""
题目二：不修改数组找出重复的数字

在一个【长度为n+1】的数组里的所有数字都在【1～n的范围内】，所以数组中至少有一个数字是重复的。
请找出数组中【任意一个】重复的数字，但不能修改输入的数组。
例如，如果输入长度为8的数组[2,3,5,4,3,2,6,7]，那么对应的输出是重复的数字2或者3

"""

"""
法一：
可以用数组实现一个哈希表，创建一个长度为n+1的辅助数组，则其下标为0～n，然后逐一将原数组中的数字复制到辅助数组中，数字为m，则复制到下标为m的位置
时间复杂度是O(n)，空间复杂度是O(n)

法二：二分查找
关键思想在于【某个取值范围内的数字个数】，题目中的关键条件是【数组长度为n+1，取值范围为1～n】，也就是说取值范围内有n个数字，但是数组中却又n+1个数字，一定存在重复。
只要不断缩小范围，找到存在数字个数大于取值范围的范围就好了。才用二分法缩小范围。
相当于二分查找，只不过每次二分不是比较数字大小，而是比较数字个数。
countRange将被调用O(nlogn)次，空间复杂度为O(1)，以时间换空间
【这种方法不能保证找出所有重复数字！只能找到任意一个！！！】

"""


class Solution:
    def findRepeatNumber(self, nums):
        # 首先判断输入是否合法
        # 判断输入数组是否为空
        if not nums or len(nums) <= 0:
            return None
        # 判断数组元素是否都在1～n之间
        if not set(nums).issubset(set(range(1, len(nums)))):
            return None

        # 二分查找
        start = 1
        end = len(nums) - 1  # n

        while start <= end:
            mid = start + ((end - start) >> 1)
            count = self.countRange(nums, start, mid)  # 计算前半段的数字个数

            # 递归出口
            if start == end:
                if count > 1:
                    return start

            if count > (mid - start + 1):
                end = mid
            else:
                start = mid + 1
        return None

    def countRange(self, nums, start, end):
        # 计算数组nums中有多少个数字是在start和end之间的
        if not nums:
            return 0
        count = 0
        for num in nums:
            if start <= num <= end:
                count += 1
        return count


if __name__ == '__main__':
    nums = [2,3,5,4,3,2,6,7]
    res = Solution().findRepeatNumber(nums)
    print(res)

