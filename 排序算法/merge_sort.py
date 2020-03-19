"""
    归并排序及其优化
"""

from 排序算法 import util


class MergeSort:
    def merge_sort(self, nums):
        if not nums or len(nums) <= 0:
            return []

        if len(nums) == 1:
            return nums

        mid = len(nums) // 2

        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)

    def merge(self, nums1, nums2):
        left = 0
        right = 0
        result = []

        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                result.append(nums1[left])
                left += 1
            else:
                result.append(nums2[right])
                right += 1

        if left < len(nums1):
            result.extend(nums1[left:])

        if right < len(nums2):
            result.extend(nums2[right:])

        return result


class MergeSortOptimize:
    def merge_sort(self, nums):
        if len(nums) < 2:
            return
        self._merge_sort(nums, 0, len(nums)-1)
        return nums

    def merge(self, nums, start, mid, end):
        """"
            合并两个有序数组
        """

        help_nums = []
        left_ptr = start
        right_ptr = mid + 1

        while left_ptr <= mid and right_ptr <= end:
            if nums[left_ptr] < nums[right_ptr]:
                help_nums.append(nums[left_ptr])
                left_ptr += 1
            else:
                help_nums.append(nums[right_ptr])
                right_ptr += 1

        while left_ptr <= mid:
            help_nums.append(nums[left_ptr])
            left_ptr += 1

        while right_ptr <= end:
            help_nums.append(nums[right_ptr])
            right_ptr += 1

        # 再把复制的数组还原到原数组
        for i in range(len(help_nums)):
            nums[start + i] = help_nums[i]

    def _merge_sort(self, nums, start, end):
        """"
            归并排序的递归实现
        """
        if start == end:
            return

        mid = (start + end) // 2
        self._merge_sort(nums, start, mid)
        self._merge_sort(nums, mid+1, end)
        self.merge(nums, start, mid, end)


if __name__ == '__main__':
    test_time = 100
    max_size = 10
    max_value = 100
    min_value = 0

    for i in range(test_time):
        # 生成数字范围在0～100的数组
        nums1 = util.get_random_array(max_size, min_value, max_value)
        print("排序前数组：", nums1)

        nums2 = nums1.copy()

        # 对数组进行排序
        MergeSortOptimize().merge_sort(nums1)
        print("排序后数组：", nums1)

        if nums1 != sorted(nums2):
            print("排序失败")
            print("the false example is {}".format(nums1))
            print("the result of the false is {}".format(nums1))
            break


if __name__ == '__main__':
    test_time = 100
    max_size = 10
    max_value = 100
    min_value = 0

    for i in range(test_time):
        # 生成数字范围在0～100的数组
        nums1 = util.get_random_array(max_size, min_value, max_value)
        print("排序前数组：", nums1)

        nums2 = nums1.copy()

        # 对数组进行排序
        nums1 = MergeSortOptimize().merge_sort(nums1)
        print("排序后数组：", nums1)

        if nums1 != sorted(nums2):
            print("排序失败")
            print("the false example is {}".format(nums1))
            print("the result of the false is {}".format(nums1))
            break
