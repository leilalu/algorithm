"""
统计一个数字在排序数组中出现的次数。

 

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0

"""


class Solution1:
    def search(self, nums, target):
        """"
            第一种方法 哈希表法

            时间复杂度是O(logn)
        """
        if not nums:
            return 0

        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1

        if target in num_count:
            res = num_count[target]
        else:
            res = 0

        return res


class Solution2:
    def search(self, nums, target):
        """"
            二分查找，查找数字的左右边界，然后返回边界之差
        """
        if not nums:
            return 0

        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        if left == right == -1:
            return 0
        else:
            return right - left + 1

    def searchLeft(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) >> 1)

            if nums[mid] == target:
                if mid == 0 or nums[mid] > nums[mid-1]:
                    return mid
                else:
                    right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def searchRight(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid] < nums[mid+1]:
                    return mid
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


if __name__ == '__main__':
    nums = [5,7,7,8,8,10]
    target = 8
    res = Solution2().search(nums, target)
    print(res)