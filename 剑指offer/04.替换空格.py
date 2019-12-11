"""
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

"""
import re


class Solution:
    # s 源字符串
    def replaceSpace_1(self, s):
        """
        暴力法：
            先将字符串按空格分开得到单词序列，再使用【%20】进行连接

        缺陷：当存在连续的空格时，无法识别；
             当字符串前存在空格时，无法识别；

        :param s:
        :return:
        """
        if not s:
            return ""
        if " " not in s:
            return s
        word_list = s.split(" ")
        res = ""
        for word in word_list:
            res = res + word + "%20"
        res = res[:-3]
        return res

    def replaceSpace_2(self, s):
        """
            python字符串的内置函数

        :param s:
        :return:
        """
        res = s.replace(' ', '%20')
        return res

    def replaceSpace_3(self, s):
        """
            使用正则表达式

        :param s:
        :return:
        """
        ret = re.compile(' ')
        res = ret.sub('%20', s)
        return res


if __name__ == '__main__':
    s = "  We Are Happy"
    # s = ""
    # s = "wehappy"
    solution = Solution()
    res = solution.replaceSpace_3(s)
    print(res)
