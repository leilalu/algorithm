class Solution:
    def reversePairs(self, nums):
        if not nums or len(nums) <= 1:
            return 0

        copy = [num for num in nums]

        count = self.reversePairsCore(nums, copy, 0, len(nums)-1)

        return count

    def reversePairsCore(self, nums, copy, begin, end):
        if begin == end:
            copy[begin] = nums[begin]
            return 0

        length = (end - begin) // 2

        left = self.reversePairsCore(copy, nums, begin, begin+length)
        right = self.reversePairsCore(copy, nums, begin+length+1, end)

        i = begin + length
        j = end

        indexCopy = end
        count = 0

        while i >= begin and j >= begin+length+1:
            if nums[i] > nums[j]:
                copy[indexCopy] = nums[i]
                indexCopy -= 1
                i -= 1
                count += j - begin - length

            else:
                copy[indexCopy] = nums[j]
                indexCopy -= 1
                j -= 1

        while i >= begin:
            copy[indexCopy] = nums[i]
            indexCopy -= 1
            i -= 1

        while j >= begin + length + 1:
            copy[indexCopy] = nums[j]
            indexCopy -= 1
            j -= 1

        return count + left + right

