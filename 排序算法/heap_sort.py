"""
堆：是一种特殊的树

满足条件：
    1）堆是一个完全二叉树
        完全二叉树：除了最后一层，其他层的节点个数都是满的，最后一层的节点都靠左排列。
    2）堆中每一个节点的值都必须大于等于>=（或小于等于<=）其子树中每个节点的值  ---- > 因此堆顶元素就是数组的最大值/最小值
        堆中每个节点都大于等于（或小于等于）其左右子结点的值
        每个节点的值都【大于等于】子树中每个节点值的堆，叫做【大顶堆】
        每个节点的值都【小于等于】子树中每个节点值的堆，叫做【小顶堆】

堆的存储：
    由于堆是一个完全二叉树，因此适合用数组来存储，不需要存储左右子结点的指针，单纯地通过数组的下标，就可以计算出其左右子结点和父节点的下标。
    假设数组数据是从下标1开始存储的，数组中下标为i的节点的【左子结点】是下标为 i*2 的节点，【右子结点】是下标为 i*2+1 的节点， 【父节点】是下标为 i//2 的节点。
    如果数组数据是从下标0开始存储的，数组中下标为i的节点的【左子结点】是下标为 2*i+1 的节点，【右子结点】是下标为 2*i+2的节点，【父节点】是下标为 (i-1)/2 的节点。

在堆上可以进行的操作：
    堆化的时间复杂度跟树的高度成正比 O(logn)
    因此插入数据和删除堆顶元素的时间复杂度都是O(logn)
    1.向堆中插入元素（堆化）
        从下往上堆化：
            1）先将新节点插入到数组末尾（挂在完全二叉树的最后一个位置）
            2）然后从下网上，不断与其父节点比较大小：
                如果是大顶堆，则当新节点大于父节点时，与父节点进行交换，直到新节点不大于其父节点，或达到根节点
                如果是小顶堆，则当新节点小于父节点时，与父节点进行交换，直到新节点不小于其父节点，或达到根节点

    2.删除堆顶元素(从上往下堆化)
        1）移除数组的最后一个元素，把它放到堆顶。  ---> 移除最后一个元素的好处是，不会出现数组空洞，满足完全二叉树特性
        2）然后从上往下堆化：
            如果是大顶堆，那么与比当前堆顶大的子结点交换，如果左右子结点都比它大，则与更大的那个交换，直到满足条件
            如果是小顶堆，那么与比当前堆顶小的子结点交换，如果左右子结点都比它小，则与更小的那个交换，直到满足条件

堆排序

原理：
    两大步骤：建堆、排序
    1.建堆
        首先将待排序数组原地建堆。
        1）从前往后插入数据，每次插入都从下往上堆化
        2）从后往前处理数据，每个数据都是从上往下堆化  O(n)
            从第一个非叶节点开始，从上往下堆化，然后堆化上一个非叶节点，直到根节点堆化完毕

    2.排序
        建堆结束之后，数组中的堆顶元素就是最大值
        将它与最后一个元素互换，那么最大的元素就放到了下标为n的位置
        当堆顶元素移除后，我们把剩下n-1个元素重新构建成堆（从上往下堆化），直到堆中只剩下下标为1的一个元素，排序结束。

执行效率：
    时间复杂度：
        建堆过程的时间复杂度是O(n),排序过程的时间复杂度是O(nlogn)
        堆排序整体时间复杂度是O(nlogn)

    空间复杂度：
        原地排序：O(1)

    稳定性：不稳定
        在排序过程中，存在将堆的最后一个节点，跟堆顶节点互换，导致最后一个节点跑到了堆顶，有可能会改变值相同数据的原始相对顺序。

"""

import random


def get_random_array(max_size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(max_size)]


# 最大堆
class BigHeapSort:

    # 建堆
    def buildHeap(self, nums, n):
        for i in range((n-1)//2, -1, -1):
            # 从最后一个非叶节点(n-1)//2，到根节点（0）
            self.heapify(nums, n, i)

    # 下沉建堆
    def heapify(self, nums, n, i):
        # 最大节点的下标为n，当前节点下标i
        while True:
            maxPos = i;
            # 先比较左子节点
            if i*2+1 <= n and nums[i] < nums[i*2+1]:
                maxPos = i*2+1
            if i*2+2 <= n and nums[maxPos] < nums[i*2+2]:
                maxPos = i*2+2
            # 如果子结点都比父节点小
            if maxPos == i:
                break

            nums[i], nums[maxPos] = nums[maxPos], nums[i]
            i = maxPos  # 到子结点，继续下沉

    # 堆排序
    def heap_sort(self, nums):
        # 数组元素个数小于2，无需排序
        if len(nums) < 2:
            return nums
        n = len(nums)-1  # 最后一个元素的下标
        # 建堆，将数组中每个元素插入到堆中（不好）
        self.buildHeap(nums, n)

        k = n
        while k > 0:
            nums[0], nums[k] = nums[k], nums[0]  # 最后一个元素与堆顶交换
            k -= 1
            self.heapify(nums, k, 0)  # 对堆顶元素进行下沉

        return nums


if __name__ == '__main__':
    test_time = 10  # 测试100次
    max_size = 10  # 数组最大长度
    max_value = 10  # 数组内元素最大值
    min_value = 0  # 数组内元素最小值

    for i in range(test_time):
        arr1 = get_random_array(max_size, min_value, max_value)  # 随机生成数组
        arr2 = arr1.copy()  # 验证数组
        res = BigHeapSort().heap_sort(arr1)  # 对数组排序
        print(arr1)
        if arr1 != sorted(arr2):  # 排序后数组与库函数排序后的数组进行比较
            print("the false sample is {}".format(arr2))
            print("the result of the false is {}".format(arr1))
            break




































