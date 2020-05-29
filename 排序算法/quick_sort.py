"""
快排的最坏情况是O(n*n)：
    此时原始数据本身就是有序，或接近有序的，每次分区点都选择最后一个元素（即最大的那个元素），那快排划分的两个子区间，一个为长度为0，一个为n。
    相当于每次都找到最后一个元素，退化成类似于冒泡排序之类的O(n*n)。【因此最坏情况是分区点选取不合理，使得划分的两个子区间元素个数差距太大。】

理想分区点：
    被分区点分开的两个分区中，数据的数量差不多。

原始为取最后一个元素/第一个元素作为分区点
优化：
1、三数取中法
优化方法可以从区间的首、尾、中间，分别取出一个数，然后对比大小，取这3个数的中间值作为分区点。
如果排序的数组比较大，三数取中不够，就可以进行五数取中，十数取中

2、随机法
每次随机选取一个元素作为分区点
平均情况下，分区点是好的，有可能出现退化为O(n*n)的情况，出现可能性不大

3、递归可能出现栈溢出，可以手动个设定栈的最大深度


经典题：
    求解数组中的第k个元素的问题
    可以使用快速排序的partition()实现，时间复杂度是O(n)
    比较总次数：n + n/2 + n/4 + ... 等比数列的和为 2n-1
    （该题可以使用最小堆来解决，第k个最小元素的问题）

"""

import random


def quicksort(nums):
    """非原地算法"""
    if len(nums) < 2:
        return nums
    else:
        # """非原地算法"""
        # pivot = nums[0]  # 以第一个元素作为切分点
        # less = [i for i in nums[1:] if i <= pivot]
        # greater = [i for i in nums[1:] if i > pivot]
        #
        # return quicksort(less) + [pivot] + quicksort(greater)

        """原地算法"""
        return quick_sort(nums, 0, len(nums)-1)


def quick_sort(nums, start, end):
    # 递归出口：注意不是等于 而是 start >= end 两者相等时，有一个元素，还有分区为0的时候
    if start >= end:
        return
    index = partition(nums, start, end)
    quick_sort(nums, start, index-1)
    quick_sort(nums, index+1, end)
    return nums


def partition(nums, start, end):
    if start == end:
        pivot = start
    else:
        pivot = random.randrange(start, end)

    nums[pivot], nums[end] = nums[end], nums[pivot]

    i = start
    for j in range(i, len(nums)):
        if nums[j] < nums[end]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

    nums[end], nums[i] = nums[i], nums[end]

    return i


if __name__ == '__main__':
    nums = [10, 4, 6, 7, 96, 8, 23]
    print(quicksort(nums))
