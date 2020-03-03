"""
题目：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转

输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素

"""


def FindMinNumber(rotateArray):
    if not rotateArray or len(rotateArray) == 0:
        return 0

    left = 0
    right = len(rotateArray) - 1
    mid = 0

    while rotateArray[left] >= rotateArray[right]:
        if right - left == 1:
            mid = right
            break

        mid = left + ((right - left) >> 1)

        if rotateArray[left] == rotateArray[right] == rotateArray[mid]:
            return minOrder(rotateArray, left, right)

        if rotateArray[left] <= rotateArray[mid]:
            left = mid
        elif rotateArray[right] >= rotateArray[mid]:
            right = mid

    return rotateArray[mid]


def minOrder(rotateArray, left, right):
    res = rotateArray[0]
    for i in range(left+1, right+1):
        if res > rotateArray[i]:
            res = rotateArray[i]
    return res


rotateArray = [1,1,1,0,1]
res = FindMinNumber(rotateArray)
print(res)
