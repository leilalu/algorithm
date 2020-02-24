"""
题目二：0～n-1中缺失的数字

一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不再该数组中，请找出这个数字。

"""


class Solution1:
    def GetMissingNumber(self, numbers, length):
        """
            暴力法：
                可以先计算出 0～n-1内n个数字的和 即 n(n-1)/2
                然后计算出数组中元素的和
                两和之差就是缺少的那个元素

            时间复杂度是O(n)

        :param numbers:
        :param length:
        :return:
        """
        if not numbers or length <= 0:
            return -1
        s1 = length * (length + 1) // 2
        s2 = 0
        for num in numbers:
            s2 += num
        res = s1 - s2
        return res


class Solution2:
    def GetMissingNumber(self, numbers, length):
        """
        注意到题目中的【排序数组】，要想到二分查找

            根据数组的范围和特点，我们可以发现，缺失的数字m是数组中第一个数值与下标不相等的下标，
            因此找出数组中缺失的数字就转换成了【找出排序数组中第一个值和下标不相等的元素】

        二分过程：
            如果中间元素的值和下标相等，那么下一轮只需要找右半边
            如果中间元素的值和下标不想等，
                    如果它前面一个元素和它的下标相等，那么这是数字就是我们要找的
                    如果它前面一个元素和它的下标不相等，那么下一轮需要找左半边


        """
        # 检查无效输入
        if not numbers or length <= 0:
            return -1

        left = 0
        right = length-1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if numbers[mid] == mid:
                left = mid + 1
            else:
                if mid == 0 or numbers[mid - 1] == mid - 1:
                    return mid
                right = mid - 1

        # 最后一个元素缺失
        if left == length:
            return length

        # 无效的输入，比如数组不是按要求排序的
        # 或者有数字不再0～n-1之内
        return -1


if __name__ == '__main__':
    numbers = [0,1,2,3,4,5]
    length = 6
    s = Solution2()
    res = s.GetMissingNumber(numbers, length)
    print(res)

