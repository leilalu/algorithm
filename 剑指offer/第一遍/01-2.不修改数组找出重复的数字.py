"""
题目二： 不修改数组找出重复的数字

在一个长度为n+1的数组里的所有数字都在1～n的范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但不能修改输入的数组。

例如，如果输入长度为8的数组{2，3，5，4，3，2，6，7}，那么对应的输出是重复的数字2或者3

"""


class Solution1:
    def getDuplication(self, numbers, n):
        """
            哈希表法
            看到题目中【重复】，常规做法就是哈希表，利用空间换取时间，不修改原数组，但是需要辅助哈希表

        :param numbers: 输入含有重复数字的数组
        :param length: 输入数组的长度  即n+1
        :return: 数组中任意一个重复的数字
        """

        # 判断无效输入
        if not numbers or n <= 1 or len(numbers) != n:
            # 输入数组为空 或 数组长度为1，或 小于1  或 数组长度和给定数组长度不相等
            return False

        # 数组中的数字都在1～n的范围内
        if not set(numbers).issubset(set(range(1, n))):
            return False

        hashdict = set()

        for index, item in enumerate(numbers):
            if item in hashdict:
                print(item)
                return True
            else:
                hashdict.add(item)

        return False


class Solution2:

    def getDuplication(self, numbers, n):
        """
            数组中会有重复的数字是因为：加入没有重复的数字，从1～n的范围里只有n个数字，但是数组长度是n+1，包含了超过n个数字，所以一定有重复的数字
            这个重复的数字是1～n之间的某个数，搜索空间是1～n，可以通过二分查找不断缩小搜索空间，搜索空间的一句就是范围内的数字个数。

            问题关键是【某个范围里数字的个数】

            把1～n个数字分为两部分（注意分的是1～n的数字范围，而不是输入数组），中间数字是m，前一半为1～m，后面一半是m+1～n
            如果前一半数字的数目超过m个，那么这一半的区间里一定包含重复数字，否则另一半区间里一定包含重复数字。

            时间复杂度：相当于二分查找，调用countRange函数O(logn)次，每次需要O(n)的时间，因此时间复杂度是O(nlogn)
            空间复杂度：没有使用辅助的空间，O(1)

            是以时间换空间

            但是这种算法不能保证找到所有重复的数字

        :param numbers: 输入n+1长的数组
        :param n: 数字的范围1～n
        :return:
        """
        if not numbers or n <= 1 or len(numbers) != n:
            return False

        if not set(numbers).issubset(set(range(1, n))):
            return False

        start = 1
        end = n-1

        while end >= start:
            mid = start + ((end - start) >> 1)  # 将 /2 除法运算转化为位运算，提高计算速度
            count = self.countRange(numbers, start, mid)

            if end == start:
                if count > 1:
                    return start
                else:
                    break

            if count >= (mid - start + 1):
                end = mid
            else:
                start = mid + 1

        return False

    def countRange(self, numbers, start, end):
        count = 0
        if len(numbers) == 0:
            return 0
        for i in range(len(numbers)):
            # 遍历整个数组，找到指定范围内的数字个数
            if start <= numbers[i] <= end:
                count += 1
        return count


if __name__ == '__main__':
    numbers = [2,3,5,4,3,2,6,7]
    n = 8
    s = Solution2()
    res = s.getDuplication(numbers, n)
    print(res)




