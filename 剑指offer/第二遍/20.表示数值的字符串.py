"""
题目描述
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

"""


class Solution:
    def isNumeric(self, s):
        if not s or len(s) <= 0:
            return False

        aList = [w.lower() for w in s]
        if 'e' in aList:
            indexE = aList.index('e')
            front = aList[:indexE]
            behind = aList[indexE+1:]

            if len(behind) == 0 or '.' in behind:
                return False
            else:
                isFront = self.scanDigit(front)
                isBehind = self.scanDigit(behind)

                return isFront and isBehind
        else:
            isNum = self.scanDigit(aList)
            return isNum

    def scanDigit(self, aList):
        dotNum = 0
        allowVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '.']
        for i in range(len(aList)):
            if aList[i] not in allowVal:
                return False
            if aList[i] in '+-' and i != 0:
                return False
            if aList[i] == '.':
                dotNum += 1

        if dotNum > 1:
            return False

        return True







