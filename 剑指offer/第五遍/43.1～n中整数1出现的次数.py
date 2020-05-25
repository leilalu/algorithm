"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

 

示例 1：

输入：n = 12
输出：5
示例 2：

输入：n = 13
输出：6

"""

"""

    以百位为例：

        百位数为0，情况由更高位决定，10022，百位数字出现1的情况:100-199，1100-1199，2100-2199，...9100-9199，共100*10=1000种。即高位(10) * 位置(100)
        百位数为1，情况由更高位和百位决定，10122，百位数字出现1的情况为:100-199, 1100-1199, 2100-2199,...9100-9199,10100-10122，共1000+23种。即高位(10) * 位置(100) + 低位(23)
        百位数大于1，10222，百位数出现1的情况为: 100-199, 1100-1199, ...9100-9199, 10100-10199 共1100种。即(高位(10)+1) * 位置(100)
        最终统计所有位置可能的1的情况。时间复杂度O(logn)
        
"""
class Solution:
    def countDigitOne(self, n):

        if n < 0:
            return 0

        count = 0
        digit = 1

        while n // digit != 0:
            high = n // (digit * 10)
            cur = (n // digit) % 10
            low = n - (n // digit) * digit

            if cur == 0:
                count += high * digit
            elif cur == 1:
                count += high * digit + low + 1
            else:
                count += (high+1) * digit

            digit *= 10

        return count


class Solution2:
    def countDigitOne(self, n):
        if n < 1:
            return 0
        count = 0
        for num in range(1, n+1):
            count += self.countOfOne(num)

        return count

    def countOfOne(self, num):
        count = 0
        while num:
            if num % 10 == 1:
                count += 1
            num //= 10

        return count


if __name__ == '__main__':
    n = 12
    res = Solution2().countDigitOne(n)
    print(res)




