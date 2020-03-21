"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，
但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""


class Solution:
    def isNumber(self, s):
        if not s or len(s) <= 0:
            return False

        charList = [w.lower() for w in s]
        if 'e' in charList:
            indexE = charList.index('e')
            front = charList[:indexE]
            behind = charList[indexE+1:]

            if len(front) == 0:
                return False

            if len(behind) == 0 or '.' in behind:
                return False

            isFront = self.isNumberCore(front)
            isBehind = self.isNumberCore(behind)

            return isFront and isBehind
        else:

            return self.isNumberCore(charList)

    def isNumberCore(self, charList):
        dotNum = 0
        allow = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.']
        for index, item in enumerate(charList):
            if item not in allow:
                return False
            if item in '+-' and index != 0:
                return False
            if item == '.':
                dotNum += 1
        if dotNum > 1:
            return False

        return True





