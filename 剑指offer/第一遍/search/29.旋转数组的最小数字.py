"""
题目描述

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个【非递减排序】的数组的一个【旋转】，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

"""


class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        """
        暴力法：遍历所有的元素
            观察旋转数组，旋转数组最大的元素应该与最小的元素相邻，且最大值在左，最小值在右，即左边大于右边
            原数组是从左到右非递减的，即左边小于右边
            因此找到旋转数组中左边大于右边的地方就能找到最小值。

            需要注意的是，由于数组是非递减的，因此当最大值与最小值相等时，整个数组的元素都相等，都只有一个数，直接返回这个数即可。

            时间复杂度是O(n)
            空间复杂度是O(1)

        """
        if len(rotateArray) == 0:
            return 0
        for i in range(len(rotateArray)):
            if rotateArray[i] < rotateArray[i-1]:
                return rotateArray[i]
        # 最大值和最小值相等
        return rotateArray[0]


class Solution2:
    def minNumberInRotateArray(self, rotateArray):
        """
        二分法：
        看到排序数组应该想到二分查找
            观察旋转数组特点，旋转数组可以划分为两个排序数组，并且前面的子数组的元素都大于或者等于后面子数组的元素。最小值恰好是这两个元素的分界线
            首元素应该大于或者等于最后一个元素 故 rotateArray[left] >= rotateArray[right]

            如果中间元素位于前面的递增子数组，那么它应该大于或者等于首元素，最小值应该在中间元素右侧 left = mid left仍然在前面的递增子数组
            如果中间元素位于后面的递增子数组，那么它应该小于或者等于尾元素，最小值应该在中间元素左侧 right = mid right仍然在后面的递增子数组

            最终left指向前面数组的最后一个元素，right指向后面数组的第一个元素，即为最小值，达到循环结束的条件。
            最终返回右边的元素

        需要注意的特例：
            1、如果把排序数组的前面0个元素搬到最后面，那么还是排序数组本身，应该返回第一个元素 因此把【mid初始化为0】

        采用了二分查找，因此时间复杂度是O(logn)
        空间复杂度是O(1)

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
            mid = left + ((right - left) >> 1)

            # 如果 下标为 left right 和 mid 的三个元素相等
            # 则只能采取顺序查找
            if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                return self.minInOrder(rotateArray, left, right)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid

        return rotateArray[mid]

    def minInOrder(self, rotateArray, start, end):
        res = rotateArray[0]
        for i in range(start+1, end+1):
            if res > rotateArray[i]:
                res = rotateArray[i]
        return res


if __name__ == '__main__':
    rotateArray = [1, 0, 1, 1, 1, 1]
    s = Solution2()
    res = s.minNumberInRotateArray(rotateArray)
    print(res)