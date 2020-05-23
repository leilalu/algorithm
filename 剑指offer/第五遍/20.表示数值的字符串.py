"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。

"""


class Solution:
    def isNumber(self, s):
        # 首先判断输入是否合法
        if not s:
            return False

        charList = [c.lower() for c in s]

        if 'e' in charList:
            indexE = charList.index('e')

            left = charList[:indexE]
            right = charList[indexE+1:]

            # 如果没有左半部，但是有E，那么不是
            if len(left) == 0:
                return False

            # 已知存在了E，那么一定得有右半部，右半部是整数，不能有小数点
            if len(right) == 0 or '.' in right:
                return False

            else:
                leftIsNumber = self.isNumberCore(left)
                rightIsNumber = self.isNumberCore(right)

                return leftIsNumber and rightIsNumber

        else:
            return self.isNumberCore(charList)


    def isNumberCore(self, charList):
        dotNum = 0
        allowList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.']
        for i in range(len(charList)):
            if charList[i] not in allowList:
                return False

            if charList[i] in '+-' and i != 0:
                return False

            if charList[i] == '.':
                dotNum += 1
        if dotNum > 1:
            return False

        return True
