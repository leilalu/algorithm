"""
题目描述
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。

"""


class Solution1:
    def NumberOf1Between1AndN_Solution(self, n):
        """"
            计算1～n中每个整数包含的1的个数，再把它们累加起来

            计算一个整数中包含的1的个数：
                当n > 0 时，循环操作：
                    1、先对该整数取余，判断个位数是不是1，如果是1，计数+1
                    2、再对该证书除以10，去掉个位，得到新的个位数

            整数n将会有logn位数，逐位判断该位是不是1，则计算一个整数的时间复杂度是O(logn)，
            那么判断n个数的时间复杂度是O(nlogn)，时间复杂度过高，不满足要求

        """
        count = 0

        for i in range(1, n+1):
            count += self.NumberOf1(i)

        return count

    def NumberOf1(self, n):
        count = 0
        while n:
            if n % 10 == 1:  # 个位数是 1
                count += 1
            n = n // 10

        return count


# class Solution2:
#     def NumberOf1Between1AndN_Solution(self, n):
#





















