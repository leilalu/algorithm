"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

"""


class Solution1:
    def Find(self, target, array):
        """

        暴力法：
            遍历整个二维数组，如果找到该整数，直接返回True，如果遍历结束没有找到该整数，返回False

            时间复杂度是O(n*n) 会超时

        :param target: 整数
        :param array: 二维数组
        :return: True or False

        """

        if not array:
            return False

        for row in array:
            for item in row:
                if item == target:
                    return True

        return False


class Solution2:
    # 左下角/右上角
    def Find(self, target, array):
        """
            充分利用二维数组中元素的大小排列顺序，如果当前位置的元素比target小，那么就向右移动，如果当前位置的元素比target大，那么就向上移动，
            直到找到target或到边界无法再移动

        :param target: 整数
        :param array: 二维数组
        :return: True or False

        """

        if not array:
            return False

        m = len(array)
        n = len(array[0])

        row = m - 1
        col = 0

        while row >= 0 and col <= n-1:
            if array[row][col] > target:
                row -= 1
            elif array[row][col] < target:
                col += 1
            else:
                return True

        return False


if __name__ == '__main__':
    target = 7
    array = [[1, 2, 3, 4],
             [5, 6, 7, 8],
             [10, 11, 12, 13]]
    s = Solution2()
    res = s.Find(target, array)
    print(res)


