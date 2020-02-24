"""
题目三：数组中数值和下标相等的元素

假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实现一个函数，找出数组中任意一个数值等于其下标的元素。

例如，在数组[-3,-1,1,3,5]中，数字3和它下标相等。

"""


class Solution1:
    def GetNumberSameAsIndex(self, numbers):
        """
            暴力法，顺序遍历数组

        """

        # 检查无效输入
        if not numbers:
            return
        for i in range(len(numbers)):
            if numbers[i] == i:
                return i

        return None



class Solution2:
    def GetNumberSameAsIndex(self, numbers):
        """
        看到【排序数组】想【二分查找】

        二分过程：
            1、如果mid的【值小于下标】，那么它左边的值都会小于他们的下标，下一轮在右半边搜索
            2、如果mid的【值大于下标】，那么它右边的值都会大于他们的下标，下一轮在左半边搜索
            3、如果mid的值等于下标，那么返回这个数

        """

        # 检查无效输入
        if not numbers:
            return

        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if numbers[mid] > mid:
                right = mid - 1
            elif numbers[mid] < mid:
                left = mid + 1
            else:
                return mid

        return -1
