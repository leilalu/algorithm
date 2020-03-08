"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。

 

示例 1:

输入: [10,2]
输出: "102"
示例 2:

输入: [3,30,34,5,9]
输出: "3033459"
 

提示:

0 < nums.length <= 100
说明:

输出结果可能非常大，所以你需要返回一个字符串而不是整数
拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

"""
from functools import cmp_to_key


class Solution:
    def minNumber(self, nums):
        # 检查无效输入
        if not nums or len(nums) <= 0:
            return ''
        # 将所有数字存放在一个字符串数组中
        strList = []
        for i in nums:
            strList.append(str(i))

        # key 是一种比较规则
        # 比较x+y和y+x
        key = cmp_to_key(lambda x, y: int(x+y) - int(y+x))

        strList.sort(key=key)

        return ''.join(strList)


if __name__ == '__main__':
    nums = [3,30,34,5,9]
    res = Solution().minNumber(nums)
    print(res)