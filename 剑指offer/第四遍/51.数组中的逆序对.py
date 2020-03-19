"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

输入: [7,5,6,4]
输出: 5

"""


class Solution:
    def reversePairs(self, nums):
        if not nums or len(nums) <= 0:
            return 0

        copy = [num for num in nums]

        start = 0
        end = len(nums) - 1

        count = self.reversePairsCore(nums, copy, start, end)

        return count

    def reversePairsCore(self, nums, copy, start, end):
        if start == end:
            copy[start] = nums[start]
            return 0

        # 注意这里不是全部数组长度除以二，而是start和end之间的数组长度
        length = (end - start) // 2

        left = self.reversePairsCore(copy, nums, start, start+length)
        right = self.reversePairsCore(copy, nums, start+length+1, end)

        p1 = start + length
        p2 = end
        curIndex = end

        count = 0
        while p1 >= start and p2 >= start+length+1:
            if nums[p1] > nums[p2]:
                copy[curIndex] = nums[p1]
                count += p2 - start - length
                p1 -= 1
                curIndex -= 1
            else:
                copy[curIndex] = nums[p2]
                p2 -= 1
                curIndex -= 1

        while p1 >= start:
            copy[curIndex] = nums[p1]
            p1 -= 1
            curIndex -= 1

        while p2 >= start+length+1:
            copy[curIndex] = nums[p2]
            p2 -= 1
            curIndex -= 1

        return count + left + right






