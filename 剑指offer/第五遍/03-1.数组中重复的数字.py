"""
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
 

限制：

2 <= n <= 100000

"""

"""
法一：排序数组
先把输入的数组排序，再从头到尾遍历排序后的数组，找到相邻两数相等的数字即为重复数字。
排序数组的时间复杂度是O(nlogn),遍历数组的时间复杂度是O(n)

法二：哈希表
从头到尾扫描数组，每扫描到一个数字，就把它加到哈希表里，如果哈希表中已经存在该数组，则找到重复数字。
只需要扫描一遍数组，时间复杂度是O(n)，但是需要维护一个哈希表，空间复杂度也是O(n)

法三：交换元素，重排数组
充分利用【数组长度为n，数字范围为0～n-1】的条件，这说明当数组排序后，数组中的数字将与索引一一对应。
由于数组中有重复的数组，有些位置可能存在多个数字，同时有些位置可能没有数字。
所以我们只需要扫描数组，判断数字和索引是否相等，若不相等则进行重排：索引i，对应数字value，找到索引value对应的数字是否与value相等，若相等则重复，若不相等则交换
                                         若相等则看下一个数字
只需要从头到尾扫描一遍数组即可完成对数组的重排，时间复杂度为O(n)，由于不需要维护额外的哈希表，空间复杂度为O(1)

"""

class Solution:
    def findRepeatNumber(self, nums):
        # 首先判断输入是否合法
        # 判断输入数组是否为空
        if not nums or len(nums) <= 0:
            return None

        # 判断输入数组中的数字是否都在0～n-1之间
        if not set(nums).issubset(set(range(len(nums)))):
            return None

        for i in range(len(nums)):
            while nums[i] != i:
                value = nums[i]
                if nums[value] == value:
                    return value
                else:
                    nums[value], nums[i] = nums[i], nums[value]
        return None


if __name__ == '__main__':
    # nums = [2, 3, 1, 0, 2, 5, 3]
    nums = [3,1,2,3]
    res = Solution().findRepeatNumber(nums)
    print(res)