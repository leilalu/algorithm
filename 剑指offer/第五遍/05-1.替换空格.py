"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

 

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."
 

限制：

0 <= s 的长度 <= 10000

"""


import re

class Solution:
    def replaceSpace1(self, s):
        # 首先判断输入是否为空
        if not s:
            return ''

        res = ''

        array = s.split(' ')

        for i in range(len(array)-1):
            res += array[i] + '%20'

        res += array[-1]

        return res

    def replaceSpace2(self, s):
        if not s:
            return ''

        res = s.replace(' ', '%20')  # 返回替换后字符串，不会在原字符串上进行修改
        return res

    def replaceSpace3(self, s):
        if not s:
            return ''

        ret = re.compile(' ')
        res = ret.sub('%20', s)

        return res

    def replaceSpace4(self, s):
        if not s:
            return ''
        count = s.count(' ')  # 统计空格的数量
        s = list(s)
        p1 = len(s) - 1
        s += [-1] * count * 2  # 由于替换多数来的空间
        p2 = len(s) - 1

        while 0 <= p1 < p2:
            if s[p1] != ' ':
                s[p2] = s[p1]
                p1 -= 1
                p2 -= 1
            else:
                p1 -= 1
                s[p2] = '0'
                p2 -= 1
                s[p2] = '2'
                p2 -= 1
                s[p2] = '%'
                p2 -= 1

        return ''.join(s)


if __name__ == '__main__':
    s = " We are happy"
    res = Solution().replaceSpace4(s)
    print(res)
