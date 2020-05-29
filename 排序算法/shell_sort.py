import random


def get_random_array(max_size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(max_size)]


def shell_sort(nums):
    n = len(nums)
    h = 1

    # 得到递增的间隔
    while h < n // 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and nums[j] < nums[j-h]:
                nums[j], nums[j-h] = nums[j-h], nums[j]
                j -= h

        h = h // 3  # 缩小间隔


if __name__ == '__main__':
    test_time = 100  # 测试100次
    max_size = 10  # 数组最大长度
    max_value = 10  # 数组内元素最大值
    min_value = 0  # 数组内元素最小值
    for i in range(test_time):
        arr1 = get_random_array(max_size, min_value, max_value)  # 随机生成数组
        arr2 = arr1.copy()  # 验证数组
        shell_sort(arr1)  # 对数组排序
        print(arr1)
        if arr1 != sorted(arr2):  # 排序后数组与库函数排序后的数组进行比较
            print("the false sample is {}".format(arr2))
            print("the result of the false is {}".format(arr1))
            break


