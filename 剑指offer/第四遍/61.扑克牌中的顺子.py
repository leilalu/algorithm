"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True

"""


class Solution:
    def isStraight(self, nums):
        if not nums or len(nums) < 5:
            return False
        countZero = 0
        countGap = 0

        nums.sort()

        i = 0
        while nums[i] == 0:
            countZero += 1
            i += 1

        small = i
        big = small + 1
        while big < len(nums):
            if nums[small] == nums[big]:
                return False
            countGap += nums[big] - nums[small] - 1
            big += 1
            small += 1

        return True if countZero <= countGap else False



if __name__ == '__main__':
    nums = [4,7,5,9,2]
    res = Solution().isStraight(nums)
    print(res)





