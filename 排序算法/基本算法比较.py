"""
基本排序算法实现
        最好时间复杂度     最坏时间复杂度     平均时间复杂度     空间复杂度       稳定性
冒泡          O(n)            O(n^2)          O(n^2)          O(1)            稳定

插入          O(n)            O(n^2)          O(n^1)          O(1)            稳定

选择          O(n^2)          O(n^2)          O(n^2)          O(1)            不稳定

"""


class Sort:
    # 冒泡排序
    def Bubble_sort(self, nums):
        # 首先判断数组长度，当数组为空、数组长度为1时，不需要排序，直接返回
        if not nums or len(nums) <= 1:
            return nums

        n = len(nums)
        # 外层循环表示在排第几个数，有几个数，外层循环多少次
        for i in range(n):
            # 如果循环没有进行任何交换操作，则说明已经排好序了，可以提前退出循环
            flag = False
            # 内层循环表示从开头比到已排序位置之前，前面已经排了i个了
            for j in range(n-i-1):
                # 出现逆序对，交换
                if nums[j] > nums[j+1]:
                    flag = True
                    value = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = value

            if not flag:
                break

        return nums

    def Insert_sort(self, nums):
        if not nums or len(nums) <= 1:
            return nums

        n = len(nums)

        for i in range(1, n):
            # 记录当前数字
            value = nums[i]
            # 记录上一个数字的位置
            j = i-1
            # 找到第一个与该数字相等或者比该数字小的数字
            while j >= 0:
                # 如果前面的数字比当前数字大，前面数字向后移
                if nums[j] > value:
                    nums[j+1] = nums[j]
                else:
                    break

                j -= 1
            # 插入数据
            nums[j+1] = value

        return nums

    def Select_sort(self, nums):
        if not nums or len(nums) <= 1:
            return nums

        n = len(nums)

        for i in range(n):
            minValue = nums[i]
            minIndex = i
            for j in range(i, n):
                if nums[j] < minValue:
                    minValue = nums[j]
                    minIndex = j

            nums[minIndex] = nums[i]
            nums[i] = minValue

        return nums



if __name__ == '__main__':
    nums = [7,6,4,6,7,2,3,1,5]
    res = Sort().Select_sort(nums)
    print(res)







