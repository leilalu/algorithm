"""
一个长度为n-1的【递增排序】数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。


示例 1:

输入: [0,1,3]
输出: 2
示例 2:

输入: [0,1,2,3,4,5,6,7,9]
输出: 8

"""


class Solution1:
    def missingNumber(self, nums):
        if not nums:
            return None

        all_numbers = [0] * (len(nums)+1)

        for num in nums:
            all_numbers[num] += 1

        for i in range(len(all_numbers)):
            if all_numbers[i] == 0:
                return i

        return None


class Solution2:
    def missingNumber(self, nums):
        if not nums:
            return None
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) >> 1)

            if nums[mid] != mid:
                if mid == 0 or nums[mid-1] == mid - 1:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1

        # 如果最后一个数也缺失
        if left == len(nums):
            return len(nums)

        return None


if __name__ == '__main__':
    nums = [0,1,2]
    res = Solution2().missingNumber(nums)
    print(res)
