"""
题目描述

请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

"""
import re


class Solution1:
    def replaceSpace(self, s):
        """
            利用辅助数组，将原字符串按空格拆分后，放入辅助数组中，再将辅助数组中的元素用'%20'拼接起来

            时间复杂度是O(n)
            空间复杂度也是O(n)

            【注意】需要注意字符串尾部的拼接

        :param s: 输入字符串
        :return: 输出替换后的字符串

        """
        # 判断无效输入 字符串为空
        if not s:
            return ''

        # 拆分字符串
        array = s.split(' ')

        # 拼接字符串
        res = ''
        for i in range(len(array)-1):
            res = res + array[i] + '%20'

        res += array[-1]

        return res


class Solution2:
    # 使用内置函数
    def replaceSpace(self, s):
        """
            python字符串的内置函数

        :param s: 输入字符串
        :return: 输出替换后的字符串

        """
        if not s:
            return ''

        res = s.replace(' ', '%20')
        return res


class Solution3:

    # 使用正则表达式
    def replaceSpace(self, s):
        """
            使用正则表达式进行空格匹配、替换
            【注意】需要引包 【import re】

        :param s: 输入字符串
        :return: 输出替换后的字符串

        """
        ret = re.compile(' ')
        res = ret.sub('%20', s)
        return res


class Solution4:
    def replaceSpace(self, s):
        """
            如果要求在原字符串上进行修改，可以将字符串看为一个字符串数组，那么要求将一个字符的空格改为三个字符的'%20'一定会导致数组的移动
            如果从前往后，每遇到一个空格，就让后续的元素向后移2格，那么对每个空格字符，需要移动后面O(n)个字符，对于含有O(n)个空格字符的字符串
            总的时间效率是O(n*n)

            问题的关键在于，如果【减少元素移动的次数】

            我们可以【从后往前】进行替换。
            先查出字符串中有多少个空格。我们已经知道一个空格要换成'%20'需要多2个空间，那么有n个空格，数组就扩充n*2的空间
            因此我们可以先扩充数组，并使用两个指针，一个指针指向新数组最后，另一个指针指向原数组最后。
            当没有遇到空格的时候，将原数组指针指向的元素复制到新数组指针指向的位置，两个指针同时前进
            当遇到空格时，原数组指针向前前进一位，新数组指针前进3位，并复制'%20'
            当原数组指针与新数组指针相遇时，说明数组扩充结束，替换完毕。

            时间复杂度是O(n)
            空间复杂度是O(1)

            tips: 将字符串转换为数组可以用 list(str)
                  将数组转换为字符串可以用 ''.join(list)

        :param s:
        :return:
        """

        if not s:
            return ''
        # 计算字符串中的空格个数
        count = s.count(' ')
        if count == 0:
            return s

        # 将字符串转化为数组
        s = list(s)
        p1 = len(s)-1
        s += [0] * count * 2
        p2 = len(s)-1

        while 0 <= p1 < p2:  # 一定不能忘了 p1 >= 0 因为当开头是空格时，p1 会减到-1 p2会减到0 此时 p2 > p1仍成立，但是p1>=0 不成立
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
    s = " We Are   Happy "
    # s = '   '
    sol = Solution4()
    res = sol.replaceSpace(s)
    print(res)
