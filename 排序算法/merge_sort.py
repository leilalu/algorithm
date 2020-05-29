import random


def get_random_array(max_size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(max_size)]


class MergeSort:
    # 按顺序合并两个有序数组，并返回排序后的新数组
    def merge(self, nums1, nums2):
        left = 0
        right = 0

        result = []  # 辅助数组，返回结果

        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:  # 保留等号是为了保证排序的稳定性
                result.append(nums1[left])
                left += 1
            else:
                result.append(nums2[right])
                right += 1

        while left < len(nums1):
            result.append(nums1[left])
            left += 1

        while right < len(nums2):
            result.append(nums2[right])
            right += 1

        return result

    def merge_sort(self, nums):
        # 递归出口，只有一个元素，直接返回
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2

        left = self.merge_sort(nums[:mid])  # 将左半部分排序，产生一个新的有序子数组
        right = self.merge_sort(nums[mid:])  # 将右半部分排序，产生一个新的有序子数组
        return self.merge(left, right)


class MergeSortOptimize:
    def merge_sort(self, nums):
        if len(nums) < 2:
            return

        self._merge_sort(nums, 0, len(nums) - 1)

    def merge(self, nums, start, mid, end):
        """合并两个有序数组"""
        help_nums = []  # 辅助数组
        left = start
        right = mid + 1

        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                help_nums.append(nums[left])
                left += 1
            else:
                help_nums.append(nums[right])
                right += 1

        while left <= mid:
            help_nums.append(nums[left])
            left += 1

        while right <= end:
            help_nums.append(nums[right])
            right += 1

        # 拷贝回原数组
        for i in range(len(help_nums)):
            nums[start+i] = help_nums[i]   # 注意 是 start+i，因为起始位置不一定是从头开始的

    def _merge_sort(self, nums, start, end):
        """归并算法递归实现"""
        # 递归出口：数组中只有一个元素
        if start == end:
            return

        mid = start + ((end - start) >> 1)
        self._merge_sort(nums, start, mid)
        self._merge_sort(nums, mid+1, end)
        self.merge(nums, start, mid, end)


if __name__ == '__main__':
    test_time = 100  # 测试100次
    max_size = 10  # 数组最大长度
    max_value = 10  # 数组内元素最大值
    min_value = 0  # 数组内元素最小值
    for i in range(test_time):
        arr1 = get_random_array(max_size, min_value, max_value)  # 随机生成数组
        arr2 = arr1.copy()  # 验证数组

        MergeSort().merge_sort(arr1)
        print(arr1)

        if arr1 != sorted(arr2):  # 排序后数组与库函数排序后的数组进行比较
            print("the false sample is {}".format(arr2))
            print("the result of the false is {}".format(arr1))
            break

    # nums = [2,5,3,0,2,3,0,3]
    # res = MergeSort().merge_sort(nums)
    # print(res)

