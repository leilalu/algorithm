"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0

"""
"""
注意，旋转数组也是部分排序数组，当要求在排序数组或部分排序数组中查找一个数字（本题查找最小的数字），或者统计某个数字出现的次数，
那么我们都可以用二分查找算法
 
"""

class Solution:
    def minArray(self, numbers):
        # 首先判断输入是否合法
        if not numbers or len(numbers) <= 0:
            return None

        # 采用二分查找，天然条件，最左边的元素大于等于最右边的元素
        left = 0
        right = len(numbers) - 1
        mid = 0  # 当输入数组不是旋转数组时，为普通排序数组
        while numbers[left] >= numbers[right]:
            if right - left == 1:
                mid = right
                break

            mid = left + ((right - left) >> 2)
            if numbers[mid] == numbers[left] == numbers[right]:
                # 逐一判断
                minValue = numbers[left]
                for i in range(left, right + 1):
                    if numbers[i] < minValue:
                        minValue = numbers[i]
                return minValue

            elif numbers[mid] >= numbers[left]:
                left = mid

            elif numbers[mid] <= numbers[right]:
                right = mid

        return numbers[mid]


