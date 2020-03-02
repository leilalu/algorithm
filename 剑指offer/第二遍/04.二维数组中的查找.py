"""
题目：
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排列。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

"""


def FindNumber(array, target):
    if not array or not target:
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


