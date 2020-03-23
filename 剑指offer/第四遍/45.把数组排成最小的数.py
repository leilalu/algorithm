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

"""
from functools import cmp_to_key


class Solution:
    def minNumber(self, nums) -> str:
        if not nums:
            return ''
        strList = [str(num) for num in nums]
        key = cmp_to_key(lambda x, y: int(x+y) - int(y+x))

        strList.sort(key=key)

        return ''.join(strList)
