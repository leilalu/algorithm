"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""


class Solution:
    def minNumberInRotateArray_1(self, rotateArray):
        """
        暴力法：
        观察旋转数组的特点，在旋转数组中，原数组的最大值和最小值应该相邻，且最大值在左，最小值在右。
        而数组中的其他元素均是左边小右边大，因此找到左边大右边小的，就能找到最小值。
        需要注意的是，由于数组是非递减排序的，所以当最大值与最小值相等时，整个数组的值都相等，因此我们不需要考虑相等的情况。

        :param rotateArray:
        :return:
        """
        if len(rotateArray) == 0:
            return 0

        for index in range(len(rotateArray)):
            if rotateArray[index] < rotateArray[index - 1]:
                return rotateArray[index]

        return rotateArray[0]

    def minNumberInRotateArray_2(self, rotateArray):
        """
        二分法：
        看到排序数组，应该想到用二分法进行查找。
        分析旋转数组的端点值，旋转数组的首元素肯定不小于尾元素，设置中间点。
        如果中间点大于首元素，说明最小的数字在后边一半，
        如果中间点小于尾元素，说明最小的数字在前边一半。

        :param rotateArray:
        :return:
        """
        if len(rotateArray) == 0:
            return 0

        left = 0
        right = len(rotateArray) - 1

        while left < right:
            mid = (left + right) // 2
            if rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                left = mid + 1

        return rotateArray[left]


if __name__ == '__main__':
    rotateArray = [3,4,5,1,2]
    s = Solution()
    res = s.minNumberInRotateArray_2(rotateArray)
    print(res)