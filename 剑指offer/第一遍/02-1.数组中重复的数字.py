"""
题目描述

在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。

例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

"""


class Solution1:
    def duplicate(selfs, numbers, duplication):
        """
            看到数组中的【重复】，考虑将数组转化为哈希表，数组元素为key，数组元素第一次出现的索引为value。
            从头到尾扫描数组的每个数字，每扫描到一个数字，用O(1)的时间判断哈希表里是否已经包含了该数字。
            如果哈希表里还没有这个数字，就把它加入哈希表；如果哈希表里已经存在了该数字，就意味着找到了一个重复数字，将这个数字返回。
            时间复杂度是O(n) 空间复杂度是O(n)

            需要对输入数组进行的判断：
                1、n < 0 时 输入不合法 返回False
                2、数组为空、 n=0 返回False
                2、n 与 数组长度是否相等 若不相等 返回False

            优点：【先将数组排序，再遍历数组】方法的时间复杂度是O(nlogn)，这种方法的时间复杂度是O(n)，略好一点，
            缺点：利用空间换时间，空间复杂度是O(n)
                 并且没有利用题目中【数字在0~n-1范围内】的条件。


        :param numbers: 输入数组长度
        :param duplication: 含有重复数字的数组
        :return: 数组中任意一个重复的数字

        """
        # 判断输入是否合法
        if not duplication or numbers <= 0 or numbers != len(duplication):
            return False

        # 无效输入：长度为n的数组中[包含] 0~n-1之外的数字
        if not set(duplication).issubset(set(range(numbers))):
            return False

        # 为输入数组构建哈希表
        hashdict = {}
        for index, item in enumerate(duplication):
            if item in hashdict:
                # 存在重复数字
                duplication[0] = item
                return True
            else:
                hashdict[item] = index

        return False


class Solution2:
    def duplicate(self, numbers, duplication):
        """
            需要注意题目中给出的【数组长度】和数组中【数字的范围】！

            根据【数组长度为n，即下标索引为0～n-1，而且数组中的数字范围为0~n-1】条件可以看出，如果数组中没有重复的数字，
            那么当数组排序之后数字i将出现在下标为i的位置。即索引为3的元素应该是数字3。

            由于数组中有重复的数字，有些位置可能存在多个数字，同时有的位置可能没有数字。

            因此可以对数组中数字进行重排复位，从头到尾依次扫描这个数字中的每个数字。当扫描到下标为i的数字m时，首先比较这个数字是不是等于i。
            如果是，则接着扫描下一个数字；如果不是，则再拿它和下标为m的数字进行比较。
                                                如果它和第m个数字相等，说明第m个数字就是m，放对了，则找到了一个重复的数字
                                                如果它和第m个数字不相等，说明第m个数字也放错了，就把第i个数字和第m个数字互换
                                                    从而第m个数字将复位

            时间复杂度：虽然有一个两重循环，但是每个数字最多只要交换两次就能找到属于它自己的位置，因此总的时间复杂度是O(n)
            空间复杂度：所有的操作步骤都是在原输入数字上进行的，不需要额外分配内存，因此空间复杂度是O(1)


        :param numbers: 输入数组长度
        :param duplication: 含有重复数字的数组
        :return: 数组中任意一个重复的数字
        """

        # 对输入参数进行判断
        if not duplication or numbers <= 0 or len(duplication) != numbers:
            return False

        # 无效输入：长度为n的数组中[包含] 0~n-1之外的数字
        if not set(duplication).issubset(set(range(numbers))):
            return False

        for i in range(len(duplication)):
            # 遍历数组
            while duplication[i] != i:
                value = duplication[i]
                if duplication[value] == value:
                    # 发现重复数字
                    duplication[0] = value
                    return True
                else:
                    # 交换位置
                    duplication[i], duplication[value] = duplication[value], duplication[i]
                    # duplication[i] = duplication[value]
                    # duplication[value] = value
        return False


if __name__ == '__main__':
    numbers = 4
    duplication = [0, 1, 2, 5]
    s = Solution2()
    res = s.duplicate(numbers, duplication)
    print(res)
