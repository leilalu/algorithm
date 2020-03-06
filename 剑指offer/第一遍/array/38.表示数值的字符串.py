"""
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

"""
import re


class Solution:
    def isNumeric(self, s):
        """
            首先将字符串转化为一个list，并且将大写转化为小写(E--->e)
            然后根据e是否存在对list进行划分。如果存在，则分为AB和C；如果不存在，则全部为AB
            如果是AB 和 C，则除了判断C是不是数字之外，还要判断C部分是否有小数点，是否没有数字
            如果是AB 则只需要判断是不是数字即可

            是不是数字要判断：1、可选字符只有0-9和+- e
                           2、最多只能有一个小数点
                           3、正负号必须在开头
        """
        # 输入字符是空字符串、空指针
        if not s or len(s) <= 0:
            return False
        # 转化为list
        aList = [w.lower() for w in s]
        if 'e' in aList:
            indexE = aList.index('e')
            front = aList[:indexE]
            behind = aList[indexE+1:]
            if '.' in behind or len(behind) == 0:  # 如果E后面包括小数点或者没有数字
                return False
            isFront = self.scanDigit(front)
            isBehind = self.scanDigit(behind)
            return isBehind and isFront
        else:
            isNum = self.scanDigit(aList)
            return isNum

    def scanDigit(self, alist):
        dotNum = 0
        allowVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.', 'e']
        for i in range(len(alist)):
            if alist[i] not in allowVal:
                return False
            if alist[i] == '.':
                dotNum += 1
            if alist[i] in '+-' and i != 0:  # 正负号必须在开头
                return False
        if dotNum > 1:
            return False
        return True


class Solution2:
    def isNumeric(self, s):
        """"
            正则表达式法
        """
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]*)?([eE][\+\-]?[0-9]+)?$", s)


if __name__ == '__main__':
    s = '233.'
    solution = Solution()
    res = solution.isNumeric(s)
    print(res)