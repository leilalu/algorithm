"""

输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。



示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6


限制：

1 <= n < 2^31

"""


class Solution1:
    def countDigitOne(self, n):
        if n < 0:
            return 0
        count = 0
        for i in range(1, n+1):
            count += self.countOf1(i)

        return count

    def countOf1(self, n):
        count = 0
        while n:
            if n % 10 == 1:
                count += 1
            n = n // 10
        return count


class Solution2:
    def countDigitOne(self, n):
        """"
            以百位为例：

                百位数为0，情况由更高位决定，10022，百位数字出现1的情况:100-199，1100-1199，2100-2199，...9100-9199，共100*10=1000种。即高位(10) * 位置(100)
                百位数为1，情况由更高位和百位决定，10122，百位数字出现1的情况为:100-199, 1100-1199, 2100-2199,...9100-9199,10100-10122，共1000+23种。即高位(10) * 位置(100) + 低位(23)
                百位数大于1，10222，百位数出现1的情况为: 100-199, 1100-1199, ...9100-9199, 10100-10199 共1100种。即(高位(10)+1) * 位置(100)
                最终统计所有位置可能的1的情况。时间复杂度O(logn)

        """
        res = 0
        i = 1

        while n // i != 0:
            high = n // (i * 10)
            current = (n // i) % 10
            low = n - (n // i) * i

            if current == 0:
                res += high * i
            elif current == 1:
                res += high * i + low + 1
            else:
                res += (high + 1) * i

            i *= 10

        return res


if __name__ == '__main__':
    n = 12
    res = Solution2().countDigitOne(n)
    print(res)




