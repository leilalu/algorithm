"""
题目三：数组中数值和下标相等的元素

假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实现一个函数，找出数组中任意一个数值等于其下标的元素。

例如，在数组[-3,-1,1,3,5]中，数字3和它下标相等。

"""


class Solution:
    def GetNumberSameAsIndex(self, numbers):
        if not numbers or len(numbers) <= 0:
            return None

        left = 0
        right = len(numbers) - 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            if numbers[mid] == mid:
                return mid
            elif numbers[mid] > mid:
                right = mid - 1
            elif numbers[mid] < mid:
                left = mid + 1


if __name__ == '__main__':
    numbers = [-3,-1,1,3,5]
    res = Solution().GetNumberSameAsIndex(numbers)
    print(res)
