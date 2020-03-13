"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

"""
import random


class Solution:
    def getLeastNumbers(self, arr, k):
        if not arr or len(arr) <= 0 or k <= 0:
            return []
        length = len(arr)
        start = 0
        end = length-1
        index = self.Partition(arr, start, end)

        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.Partition(arr, start, end)
            else:
                start = index + 1
                index = self.Partition(arr, start, end)

        return arr[:k]

    def Partition(self, nums, start, end):
        if start == end:
            pivot = start
        else:
            pivot = random.randrange(start, end)

        nums[pivot], nums[end] = nums[end], nums[pivot]

        i = start
        for j in range(start, end):
            if nums[j] < nums[end]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[end] = nums[end], nums[i]

        return i


if __name__ == '__main__':
    arr = [3,2,1]
    k = 2
    res = Solution().getLeastNumbers(arr, k)
    print(res)