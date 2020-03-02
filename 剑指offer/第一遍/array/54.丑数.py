"""

题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。

例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

"""


class Solution1:
    def GetUglyNumber_Solution(self, index):
        """"
            一个数m是另一个数n的因子的含义是：n能被m整除，也就是 n % m == 0
            丑数只能被2、3、5整除，也就是说如果一个数能被2整除，就【连续】除以2
                                       如果一个数能被3整除，就【连续】除以3
                                       如果一个数能被5整除，就【连续】除以5
            如果最后得到的结果是1，那就是丑数，否则不是

            因此，根据以上原则我们可以设计一个函数，判断一个数是不是丑数
            然后再遍历所有的数，直到找齐所有的n个丑数为止


            问题：每个整数都需要进行取余、除法计算。即使一个数不是丑数，也要进行判断。
        """
        if not index or index <= 0:
            return 0

        count = 0
        number = 0
        while count < index:
            number += 1
            if self.IsUgly(number):
                count += 1

        return number

    def IsUgly(self, number):
        while number % 2 == 0:
            number /= 2
        while number % 3 == 0:
            number /= 3
        while number % 5 == 0:
            number /= 5

        if number == 1:
            return True
        else:
            return False


class Solution2:
    def GetUglyNumber_Solution(self, index):
        """"
        空间换时间。
            建立一个长度为n的数组，保存这n个丑数。
            在进行运算的时候，某个位置需要求得丑数一定是前面某个丑数乘以2、3或者5的结果，
            我们分别记录之前乘以2后能得到的最大丑数M2，乘以3后能得到的最大丑数M3，乘以5后能得到的最大丑数M5，
            那么下一个丑数一定是M2，M3，M5中的最小的那一个。从而使得数组是排序的
            同时注意到，已有的丑数是按顺序存放在数组中的。对乘以2而言，肯定存在某一个丑数T2，排在他之前的每一个丑数乘以2得到的结果都会小于已有的最大丑数，
            在他之后的每一个丑数乘以2得到的结果都会太大，我们只需记下这个丑数的位置，每次生成新的丑数的时候，去更新这个T2。对于3和5同理。
            
        """
        if not index or index <= 0:
            return 0
        # 创建一个排序的丑数数组，用于存放要求的丑数
        uglyNumbers = [1] * index
        nextIndex = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while nextIndex < index:
            min = self.Min(uglyNumbers[index2] * 2, uglyNumbers[index3] * 3, uglyNumbers[index5] * 5)
            uglyNumbers[nextIndex] = min

            while uglyNumbers[index2] * 2 <= uglyNumbers[nextIndex]:
                index2 += 1
            while uglyNumbers[index3] * 3 <= uglyNumbers[nextIndex]:
                index3 += 1
            while uglyNumbers[index5] * 5 <= uglyNumbers[nextIndex]:
                index5 += 1

            nextIndex += 1

        return uglyNumbers[-1]

    def Min(self, number1, number2, number3):
        if number1 < number2:
            min = number1
        else:
            min = number2

        if min > number3:
            min = number3

        return min


if __name__ == '__main__':
    index = 2
    s = Solution2()
    res = s.GetUglyNumber_Solution(index)
    print(res)






























