"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个【非递减排序】的数组的一个【旋转】，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""


class Solution:
    def minNumberInRotateArray_1(self, rotateArray):
        """
        暴力法：遍历所有的元素
        观察旋转数组，旋转数组最大的元素应该与最小的元素相邻，且最大值在左，最小值在右，即左边大于右边
        原数组是从左到右非递减的，即左边小于右边
        因此找到旋转数组中左边大于右边的地方就能找到最小值。
        需要注意的是，由于数组是非递减的，因此当最大值与最小值相等时，整个数组的元素都相等，都只有一个数，直接返回这个数即可。
        :param rotateArray:
        :return:
        """
        if len(rotateArray) == 0:
            return 0
        for i in range(len(rotateArray)):
            if rotateArray[i] < rotateArray[i-1]:
                return rotateArray[i]

        return rotateArray[0]

    def minNumberInRotateArray_2(self, rotateArray):
        """
        二分法：
        看到排序数组应该想到二分查找
        观察旋转数组特点，旋转数组可以划分为两个排序数组，并且前面的子数组的元素都大于或者等于后面子数组的元素。最小值恰好是这两个元素的分界线
        首元素应该大于或者等于最后一个元素
        如果中间元素位于前面的递增子数组，那么它应该大于或者等于首元素，最小值应该在中间元素右侧 left = mid left仍然在前面的递增子数组
        如果中间元素位于后面的递增子数组，那么它应该小于或者等于尾元素，最小值应该在中间元素左侧 right = mid right仍然在后面的递增子数组
        最终left指向前面数组的最后一个元素，right指向后面数组的第一个元素，即为最小值，达到循环结束的条件。
        :param rotateArray:
        :return:
        """

        if len(rotateArray) == 0:
            return 0

        left = 0
        right = len(rotateArray) - 1
        mid = 0
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                mid = right
                break
            mid = (left + right) // 2
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid

        return rotateArray[mid]


if __name__ == '__main__':
    rotateArray = [1, 2]
    s = Solution()
    res = s.minNumberInRotateArray_2(rotateArray)
    print(res)