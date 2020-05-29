import random


def get_random_array(max_size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(max_size)]


"""
选择排序

原理：
    将数组分为待排区间与已排序区间，初始待排区间为整个数组
    从头到尾扫描待排区间中的每个元素，找到最小的数据元素，与待排区间的第一个元素交换

执行效率：
    时间复杂度：
        不管输入数据是否有序，确定每个元素的位置时，都需要遍历后面的每个元素，找出最小的值，因此时间复杂度是O(n*n)
        比较次数: n-1 + n-2 + ... + 1  共 n * (n-1) / 2 
        交换次数：每个位置的元素都需要交换 共n次
    
    空间复杂度：
        原地排序：O(1)
        
    稳定性：
        不稳定
        比如，[5，8，5，2，9]，第一次找到最小元素2后，与第1个5交换位置，那么第一个5和中间的5的相对顺序就变了，因此不稳定

"""


def select_sort(nums):
    # 当数组中数据元素只有1个或0个时，无需排序
    if len(nums) < 2:
        return nums

    length = len(nums)
    for i in range(length-1):
        min = i
        for j in range(i+1, length):
            if nums[j] < nums[min]:
                min = j
        # 找到最小的元素下标min，与首元素交换
        nums[i], nums[min] = nums[min], nums[i]

    return nums


if __name__ == '__main__':
    test_time = 100  # 测试100次
    max_size = 10  # 数组最大长度
    max_value = 10  # 数组内元素最大值
    min_value = 0  # 数组内元素最小值
    for i in range(test_time):
        arr1 = get_random_array(max_size, min_value, max_value)  # 随机生成数组
        arr2 = arr1.copy()  # 验证数组
        select_sort(arr1)  # 对数组排序
        print(arr1)
        if arr1 != sorted(arr2):  # 排序后数组与库函数排序后的数组进行比较
            print("the false sample is {}".format(arr2))
            print("the result of the false is {}".format(arr1))
            break

