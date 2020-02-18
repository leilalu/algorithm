"""
题目描述

定义一个函数，输入两个字符串，从第一个字符串中删除在第二个字符串中出现过的所有字符

"""


class Solution:
    def DeleteString(self, str1, str2):
        # 检查无效输入
        if not str1 or not str2:
            return str1

        # 用哈希表将第二个字符串中的字符存储起来
        num_flag = {}
        for item in str2:
            num_flag[item] = True

        # 删除第一个字符串中的字符
        result = ''
        for item in str1:
            if item not in num_flag:
                result += item

        return result


if __name__ == '__main__':
    str1 = 'We are students'
    str2 = 'aeiou'
    s = Solution()
    res = s.DeleteString(str1, str2)
    print(res)


