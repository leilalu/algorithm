"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .

"""


class Solution:
    def isStraight(self, nums):
        if not nums or len(nums) <= 0:
            return False

        nums = sorted(nums)

        countOfZero = 0
        countOfGap = 0

        # 先计算有多少0
        i = 0
        while i < len(nums) and nums[i] == 0:
            countOfZero += 1
            i += 1

        # 计算有多少间隔
        small = countOfZero
        big = small + 1
        while big < len(nums):
            if nums[big] == nums[small]:
                return False

            countOfGap += nums[big] - nums[small] - 1
            small = big
            big += 1

        return False if countOfGap > countOfZero else True
    

if __name__ == '__main__':
    nums = [10,11,0,12,6]
    res = Solution().isStraight(nums)
    print(res)





