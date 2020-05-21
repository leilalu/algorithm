"""
题目描述

有两个【排序】的数组A1和A2。
请实现一个函数，把A2中的所有数字插入A1中，并且所有的数字都是排序的。

"""


class Solution:
    def MergeArray(self, array1, array2):
        if not array1 and not array2:
            return None
        if not array1:
            return array2
        if not array2:
            return array1

        p1 = len(array1) - 1
        p2 = len(array2) - 1

        array1 += [-1] * len(array2)
        p3 = len(array1) - 1

        while p1 < p3:  # 出口是p1 == p3 此时已经全部排完
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
    array1 = [1, 2, 3]
    array2 = [3, 4, 5]

    res = Solution().MergeArray(array1, array2)
    print(res)
