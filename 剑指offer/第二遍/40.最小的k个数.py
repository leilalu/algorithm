"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 

限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

"""
import random


class Solution:
    def getLeastNumbers(self, arr, k):
        if not arr or len(arr) <= 0 or k > len(arr):
            return []

        start = 0
        end = len(arr) - 1

        index = self.Partition(arr, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.Partition(arr, start, end)
            else:
                start = index + 1
                index = self.Partition(arr, start, end)

        result = arr[:k]
        result = sorted(result)
        return result

    def Partition(self, arr, start, end):
        if start == end:
            pivot = start
        else:
            pivot = random.randrange(start, end)

        arr[pivot], arr[end] = arr[end], arr[pivot]
        small = start - 1

        for i in range(start, end):
            if arr[i] < arr[end]:
                small += 1
                if small != i:
                    arr[small], arr[i] = arr[i], arr[small]

        small += 1
        arr[small], arr[end] = arr[end], arr[small]
        return small

