"""
题目一：字符串中第一个只出现一次的字符

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写.

"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        """
            【与字符出现次数】有关，包括【重复】，都要考虑使用哈希表

            可以用数组构建一个简单的哈希表，表示每个一字符。字符（char）是一个长度为 8-bit 的数据类型，共有 2^8=256种字符
            可以建立一个长度为256的数组，数组的每个索引数字对应一个字符的ASCII码，索引对应的数组元素表示该字符在字符串中出现的次数。

            因此对字符串遍历两次：
                第一次：遍历字符串的每个字符，在哈希表中该字符的对应次数 加1
                第二次：遍历字符串中的每个字符，当该字符在哈希表中显示次数为1时，返回该字符的位置（用enumerate）

            该方法的时间复杂度时O(n)
            空间复杂度：由于这个数组的大小是一个常数（256），因此可以人为这种算法的空间复杂度是 O(1)

        """

        # 检查无效输入
        if not s:
            return -1

        # 用数组实现一个哈希表，由于字符占8位，共256个字符，因此创建256个
        item_count = [0] * 256
        for item in s:
            item_count[ord(item)] += 1

        for index, item in enumerate(list(s)):
            if item_count[ord(item)] == 1:
                return index

        return -1


if __name__ == '__main__':
    s = 'google'
    sol = Solution()
    res = sol.FirstNotRepeatingChar(s)
    print(res)

