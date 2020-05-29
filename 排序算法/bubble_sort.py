import random


def get_random_array(max_size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(max_size)]

"""
冒泡排序

原理：
    每次比较相邻两个元素的大小，如果逆序，则进行交换
    每次冒泡可以确定一个元素的位置
    如果一次冒泡中没有出现元素的交换，说明已经有序了，此时排序可以退出

执行效率：
    时间复杂度:
        最好情况：O(n)
            当数组有序的时候，扫描一遍元素，没有逆序，没有交换，flag仍为false，将会跳出循环，此时只是将数组遍历了一遍，比较了n次，时间复杂度为O(n)
        最坏情况：O(n*n)
            数组为逆序，发生n次冒泡，每次比较之间都会发生交换。时间复杂度为O(n*n)
        平均情况：O(n*n)
            逆序度 = 满有序度 - 初始有序度
            最好情况：初始有序度=满有序度 逆序度为0
            最差情况：初始有序度=0，逆序度=满有序度= n*(n-1) / 2
            平均情况：
                n*(n-1) / 4
            时间复杂度为O(n*n)
            
    空间复杂度：
        原地排序：O(1)
    稳定性：
        当相邻元素相等时，不发生交换，从而保证冒泡排序稳定

"""


def bubble_sort(nums):
    # 元素个数小于2，不需要排序
    if len(nums) < 2:
        return nums

    flag = False
    length = len(nums)
    for i in range(length-1, 0, -1):  # 待确定的元素
        for j in range(0, i):
            if nums[j] > nums[j+1]:  # 逆序才会出现交换。若元素相等，则不交换，以保证冒泡排序的稳定性
                flag = True  # 发生交换
                nums[j], nums[j+1] = nums[j+1], nums[j]

        if not flag:
            break

    return nums


if __name__ == '__main__':
    test_time = 100  # 测试100次
    max_size = 10  # 数组最大长度
    max_value = 10  # 数组内元素最大值
    min_value = 0  # 数组内元素最小值
    for i in range(test_time):
        arr1 = get_random_array(max_size, min_value, max_value)  # 随机生成数组
        arr2 = arr1.copy()  # 验证数组
        bubble_sort(arr1)  # 对数组排序
        print(arr1)
        if arr1 != sorted(arr2):  # 排序后数组与库函数排序后的数组进行比较
            print("the false sample is {}".format(arr2))
            print("the result of the false is {}".format(arr1))
            break


