"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45

"""

"""
不可以使用循环---->可以使用递归
不可以使用if判断---->可以使用逻辑操作符+短路

利用了Python中逻辑表达式的特点：
                多个【非零】数据进行and时，逻辑表达式的返回值是最后一个元素的值
                多个数据中如果【存在0】，返回第一个0
"""


class Solution:
    def sumNums(self, n):
        return n and n + self.sumNums(n-1)


if __name__ == '__main__':
    n = 9
    res = Solution().sumNums(n)
    print(res)
