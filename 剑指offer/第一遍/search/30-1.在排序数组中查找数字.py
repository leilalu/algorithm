"""
题目一：数字在排序数组中出现的次数

统计一个数字在排序数组中出现的次数。

例如，输入排序数组[1,2,3,3,3,3,4,5] 和 数字3。 由于3 在这个数组中出现了4次，因此输出4

"""


class Solution1:
    def GetNumberOfK(self, data, k):
        """
        暴力法：顺序查找
        时间复杂度O(n)

        """
        # 检查无效输入
        if not data or len(data) == 0:
            return 0

        count = 0
        for i in range(len(data)):
            if data[i] == k:
                count += 1
        return count


class Solution2:
    def GetNumberOfK(self, data, k):
        """
        看到排序数组，想到【二分查找】
            1、确定重复出现的数字k的第一个位置：
                先用二分查找找到k，然后判断它是不是第一个k，即它前一个元素是不是k，或者它是不是第一个元素，
                如果是第一个元素，则返回它的下标，如果不是第一个k，则第一个k在它左边 end = mid - 1 继续递归查找k
            2、确定重复出现的数字k的最后一个位置：
                先用二分查找找到k，然后判断它是不是最后一个k，即它后一个元素是不是k，或者它是不是最后一个元素，
                如果是最后一个元素，则返回它的下标，如果不是最后一个k，则最后一个k在它右边， start = mid + 1 继续递归查找k
            3、如果数组中不包括k，则最终start > end，返回-1

            4、当第一个k和第二个k均不为-1时（也就是说k存在在数组中），则返回个数 last - first + 1

        """
        if not data or len(data) == 0:
            return 0
        start = 0
        end = len(data) - 1
        count = 0
        first = self.GetFirstK(data, start, end, k)
        last = self.GetLastK(data, start, end, k)
        # 数组中存在k
        if first > -1 and last > -1:
            count = last - first + 1
        return count

    def GetFirstK(self, data, start, end, k):
        # 数组中不包括k
        if start > end:
            return -1
        mid = start + ((end - start) >> 1)
        if data[mid] == k:
            if (mid > 0 and data[mid-1] != k) or mid == 0:
                return mid
            else:
                # 不是第一个k
                end = mid - 1
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

        return self.GetFirstK(data, start, end, k)

    def GetLastK(self, data, start, end, k):
        # 数组中不包括k
        if start > end:
            return -1
        mid = start + ((end - start) >> 1)
        if data[mid] == k:
            if (mid < len(data)-1 and data[mid+1] != k) or mid == len(data) - 1:
                return mid
            else:
                start = mid + 1
        elif data[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

        return self.GetLastK(data, start, end, k)


if __name__ == '__main__':
    data = [1,2,3,3,3,3,4,5]
    k = 2
    s = Solution2()
    res = s.GetNumberOfK(data, k)
    print(res)

