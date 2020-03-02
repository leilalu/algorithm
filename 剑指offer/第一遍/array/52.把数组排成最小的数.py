"""

题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

"""
from functools import cmp_to_key


class Solution1:
    def PrintMinNumber(self, numbers):
        if not numbers or len(numbers) <= 0:
            return ''

        # 将所有数字存放在一个字符串数组中
        strList = []
        for i in numbers:
            strList.append(str(i))

        # key是一种比较规则
        # 比较 x+y 和 x-y 的大小，因为str型，需要先转成int型
        key = cmp_to_key(lambda x, y: int(x+y) - int(y+x))
        strList.sort(key=key)
        return ''.join(strList)


# class Solution2:
#     def PrintMinNumber(self, numbers):
#         """
#             使用冒泡排序
#         """
#         if not numbers or len(numbers) <= 0:
#             return ''
#
#         strNum = [str(m) for m in numbers]
#         for i in range(len(numbers) - 1):
#             for j in range(i+1, len(numbers)):
#                 if strNum[i] + strNum[j] > strNum[j] + strNum[i]:
#                     # 说明i比j大，i和j换位置
#                     strNum[i], strNum[j] = strNum[j] + strNum[i]
#
#         return ''.join(strNum)


















