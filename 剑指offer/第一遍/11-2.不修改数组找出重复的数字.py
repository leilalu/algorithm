"""
题目二： 不修改数组找出重复的数字

在一个长度为n+1的数组里的所有数字都在1～n的范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组。

例如，如果输入长度为8的数组{2，3，5，4，3，2，6，7}，那么对应的输出是重复的数字2或者3

"""


class Solution:
    def getDuplication_1(self, numbers, n):
        """
            哈希表法

        :param numbers: 输入含有重复数字的数组
        :param length: 输入数组的长度
        :return: 数组中任意一个重复的数字
        """

        # 判断无效输入
        if not numbers or n <= 1:
            return False

        if len(numbers) != n+1:
            return False

        # 数组中的数字都在1～n的范围内

        hashdict = {}

        for index, item in enumerate(numbers):
            if item in hashdict:
                print(item)
                return True
            else:
                hashdict[item] = index

        return False

    def getDuplication_2(self, numbers, n):
        """
            数组中会有重复的数字是因为：加入没有重复的数字，从1～n的范围里只有n个数字，但是数组长度是n+1，包含了超过n个数字，所以一定有重复的数字
            问题关键是【某个范围里数字的个数】
            把1～n个数字分为两部分（注意分的是1～n的数字范围，而不是输入数组），中间数字是m，前一半为1～m，后面一半是m+1～n
            如果前一半数字的数目超过m个，那么这一半的区间里一定包含重复数字，否则另一半区间里一定包含重复数字。

            时间复杂度：相当于二分查找，调用countRange函数O(logn)次，每次需要O(n)的时间，因此时间复杂度是O(nlogn)
            空间复杂度：没有使用辅助的空间，O(1)

            是以时间换空间

        :param numbers: 输入n+1长的数组
        :param n: 数字的范围1～n
        :return:
        """

        if not numbers or n <= 0:
            return False

        start = 1
        end = n
        while end >= start:
            mid = ((end - start) >> 1) + start
            count = self.countRange(numbers, n, start, mid)  # 计算前半部分的数字个数

            if end == start:
                if count > 1:
                    return start
                else:
                    break

            if count > (mid - start + 1):
                end = mid
            else:
                start = mid + 1

        return False

    def countRange(self, numbers, n, start, end):
        if not numbers:
            return 0
        count = 0
        for i in range(n+1):
            if numbers[i] >= start and numbers[i] <= end:
                count += 1
        return count


if __name__ == '__main__':
    numbers = [2,3,5,4,3,2,6,7]
    n = 7
    s = Solution()
    res = s.getDuplication_2(numbers, n)
    print(res)




