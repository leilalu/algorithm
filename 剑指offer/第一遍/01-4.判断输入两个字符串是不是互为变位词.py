"""
题目描述

在英语中，如果两个单词中出现的字母相同，并且每个字母出现的次数也相同，那么这两个单词互为变位词(Anagram)

请完成一个函数，判断输入的两个字符串是不是变位词

"""


class Solution:
    def isAnagram(self, str1, str2):
        """
            无需创建两个哈希表，只需要创建一个数组用来实现哈希表，用来统计字符串中每个字符出现的次数即可

            遍历第一个字符串时，当扫描到每个字符时，为哈希表对应的项的值增加1。
            接下来扫描第二个字符串，当扫描到每个字符串时，为哈希表对应的项的值减去1。

            如果扫描完第二个字符串后，哈希表中所有的值都是0，那么这两个字符串就互为变位词。

        """
        # 检查无效输入
        if not str1 or not str2:
            return False

        # 用一个数组实现一个哈希表
        item_count = [0] * 256

        # 记录第一个字符串中的字符及其出现的次数
        for item in str1:
            item_count[ord(item)] += 1

        # 记录第二个字符中的字符及出现的次数
        for item in str2:
            item_count[ord(item)] -= 1

        # 判断是否为变位词
        if item_count == [0] * 256:
            return True
        else:
            return False


if __name__ == '__main__':
    str1 = 'silent'
    str2 = 'listen'
    s = Solution()
    res = s.isAnagram(str1, str2)
    print(res)




