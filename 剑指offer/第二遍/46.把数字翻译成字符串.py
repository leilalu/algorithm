"""
给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 2^31

"""


class Solution:
    def translateNum(self, num):
        if num < 0:
            return -1

        # 把数字转化成字符串
        numberInString = str(num)

        return self.translateNumCore(numberInString)

    def translateNumCore(self, num):
        length = len(num)

        # counts数组存放从每一字符开始有多少种翻译方法
        counts = [0] * length
        count = 0
        # 从右到左开始翻译
        for i in range(length-1, -1, -1):
            count = 0
            # 如果不是最后一个字符
            if i < length - 1:
                count = counts[i+1]
            else:
                # 如果是最后一个字符
                count = 1

            if i < length - 1:
                # 判断第i位和第i+1位数字是否在10～25的范围内，若不再，则不加
                digit1 = int(num[i])
                digit2 = int(num[i+1])
                converted = digit1 * 10 + digit2
                if 10 <= converted <= 25:
                    if i < length - 2:
                        count += counts[i+2]
                    else:
                        count += 1
            counts[i] = count

        count = counts[0]
        return count


if __name__ == '__main__':
    num = 12258
    res = Solution().translateNum(num)
    print(res)







