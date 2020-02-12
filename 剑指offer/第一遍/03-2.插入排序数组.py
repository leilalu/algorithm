"""
题目描述

有两个排序的数组A1和A2，内存在A1的末尾有足后多的空余空间容纳A2。
请实现一个函数，把A2中的所有数字插入A1中，并且所有的数字是排序的。

"""


class Solution:
    def insertArray(self, array1, array2):
        """
         如果【从前往后】依次比较两个数组中数字的大小，并且插入，则移动次数过多，时间复杂度是O(n*n) 不满足要求

         在合并两个数组（包括字符串）时，如果从前往后复制每个数字（或字符）则需要重复移动数字（或字符）多次，那么我们可以考虑
         【从后往前】复制，这样就能减少移动的次数，从而提高效率

         【注意】在合并两个数组时，需要注意数组越界的情况：即某一个数组已经遍历完了，另一个还没有，此时应该把遍历完的数组的指针停下来

        :param array1:
        :param array2:
        :return:
        """
        if not array1:
            return array2
        if not array2:
            return array1

        # 扩充array1
        p1 = len(array1) - 1
        p2 = len(array2) - 1
        array1 += [0] * len(array2)
        p3 = len(array1) - 1

        while p1 < p3:
            if p1 >= 0 and p2 >= 0:
                if array1[p1] > array2[p2]:
                    array1[p3] = array1[p1]
                    p1 -= 1
                    p3 -= 1
                else:
                    array1[p3] = array2[p2]
                    p2 -= 1
                    p3 -= 1
            elif p1 < 0:
                array1[p3] = array2[p2]
                p2 -= 1
                p3 -= 1
            elif p2 < 0:
                array1[p3] = array1[p1]
                p1 -= 1
                p3 -= 1

        return array1


if __name__ == '__main__':
    array1 = [0, 2, 3]
    array2 = [1, 3]
    s = Solution()
    res = s.insertArray(array1, array2)
    print(res)


