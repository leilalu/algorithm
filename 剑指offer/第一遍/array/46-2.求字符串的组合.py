"""
题目描述

生成所给字符的所有组合

比如输入abc, 则他们的组合有['a', 'ab', 'abc', 'ac', 'b', 'bc', 'c'], ab和ba属于不同的排列, 但属于同一个组合

"""


class Solution:
    def group(self, ss):
        if not len(ss):
            return []
        if len(ss) == 1:
            return list(ss)

        charList = list(ss)
        charList.sort()
        result = []
        for i in range(len(charList)):
            # 长度为1的组合
            result.append(charList[i])
            # 重复字符不考虑
            if i > 0 and charList[i] == charList[i - 1]:
                continue
            # 只考虑不包含该字符的组合
            temp = self.group(''.join(charList[i + 1:]))

            # 链接所有的组合
            for j in temp:
                result.append(charList[i] + j)

            # 去除重复
            result = list(set(result))
            result.sort()
        return result