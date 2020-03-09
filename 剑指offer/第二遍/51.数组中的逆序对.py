"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

 

示例 1:

输入: [7,5,6,4]
输出: 5
 

限制：

0 <= 数组长度 <= 50000

"""


class Solution:
    def reversePairs(self, nums):
        length = len(nums)
        if not nums or length <= 0:
            return 0

        copy = [0]
        for num in nums:
            copy.append(num)

        count = self.reversePairsCore(nums, copy, 0, length-1)

        return count

    def reversePairsCore(self, nums, copy, start, end):
        if start == end:
            copy[start] = nums[start]
            return 0

        # 划分子数组
        length = (end - start) // 2

        left = self.reversePairsCore(copy, nums, start, start+length)
        right = self.reversePairsCore(copy, nums, start+length+1, end)

        i = start+length
        j = end

        indexCopy = end
        count = 0

        while i >= start and j >= start+length+1:
            if nums[i] > nums[j]:
                copy[indexCopy] = nums[i]
                indexCopy -= 1
                i -= 1
                count += j - start - length
            else:
                copy[indexCopy] = nums[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = nums[i]
            indexCopy -= 1
            i -= 1

        while j >= start+length+1:
            copy[indexCopy] = nums[j]
            indexCopy -= 1
            j -= 1

        return left + right + count


if __name__ == '__main__':
    nums = [1,3,2,3,1]
    res = Solution().reversePairs(nums)
    print(res)




