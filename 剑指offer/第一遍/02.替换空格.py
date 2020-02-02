"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

"""
import re


class Solution:
    # Brute force
    def replaceSpace_1(self, s):
        """
            使用split函数将字符串按空格切分，再使用"%20"将这些元素连接起来
        :param s: 输入字符串
        :return: 输出替换后的字符串

        """
        # 需要判断字符串 不为空
        if not s:
            return ""
        # 当字符串不为空时
        array = s.split(" ")
        res =""
        num = len(array)
        for i in range(num-1):
            res = res + array[i] + "%20"
        res += array[-1]
        return res

    # 使用内置函数
    def replaceSpace_2(self, s):
        """
            python字符串的内置函数

        :param s: 输入字符串
        :return: 输出替换后的字符串

        """
        res = s.replace(' ', '%20')
        return res

    # 使用正则表达式
    def replaceSpace_3(self, s):
        """
            使用正则表达式进行空格匹配、替换
            【注意】需要引包 【import re】

        :param s: 输入字符串
        :return: 输出替换后的字符串

        """
        ret = re.compile(' ')
        res = ret.sub('%20', s)
        return res


if __name__ == '__main__':
    s = " We Are   Happy "
    sol = Solution()
    res = sol.replaceSpace_3(s)
    print(res)
