"""
题目描述

输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

"""


import random
class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        """"
        基于 快速排序 的方法

        时间复杂度是O(n)

        """
        def quick_sort(lst):
            if not lst:
                return []
            pivot = lst[0]
            left = quick_sort([x for x in lst[1:] if x < pivot])
            right = quick_sort([x for x in lst[1:] if x >= pivot])
            return left + [pivot] + right

        if not tinput or k > len(tinput):
            return []
        tinput = quick_sort(tinput)
        return tinput[:k]


class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        """"
            基于 Partition 的方法

            时间复杂度是O(n)
        """
        n = len(tinput)
        if n <= 0 or k > n or k == 0:
            return []
        start = 0
        end = n-1
        index = self.Partition(tinput, start, end)
        while index != k-1:
            if index > k-1:
                end = index-1
                index = self.Partition(tinput, start, end)
            else:
                start = index+1
                index = self.Partition(tinput, start, end)
        res = tinput[:k]
        res = sorted(res)
        return res

    def Partition(self, array, start, end):
        if start == end:
            # 只有一个数时
            pivot = start
        else:
            pivot = random.randrange(start, end)
        # 先把基准值换到列表的最后一位上
        array[pivot], array[end] = array[end], array[pivot]
        small = start - 1
        for i in range(start, end):
            if array[i] < array[end]:
                small += 1
                if small != i:
                    # 此时 small 指向第一个大于pivot的数，i指向小于pivot的数，将他俩互换
                    array[small], array[i] = array[i], array[small]

        small += 1
        array[small], array[end] = array[end], array[small]

        return small


class Solution3:
    def GetLeastNumbers_Solution(self, tinput, k):
        """
            基于 堆排序(最大堆) 的实现：
                创建一个大小为k的数据容器来存储最小的k个数字
                1、当容器不为空的时候，直接读入容器
                2、当容器满的时候：
                    2-1、在这k个整数中【查找】最大的数----O(1)
                    2-2、将最大值与要插入的数进行比较
                        2-2-1、如果待插入的值比当前已有的最大值小，则用这个数替换当前已有的最大值
                        2-2-2、如果待插入的值比当前已有的最大值大，则抛弃这个数
                    2-3、如果需要进行替换，则【删除】最大的数----O(logk)
                    2-4、【插入】待插入的值------O(logk)

            使用【最大堆】存放k个数字：最大堆中，根结点的值总是大于它的子树中任意结点的值，可以实现O(1)时间内完成查找

            还可以使用【红黑树】来做

            时间复杂度是O(nlogk)

            这种方法不需要在原数组上进行修改，适合海量数据的输入【从海量数据中找出最小的k个数字】

        """
        def siftup(lst, temp, begin, end):
            if not lst:
                return []
            # i 为根结点，j为右子结点
            i, j = begin, begin * 2 + 1

            while j < end:
                if j + 1 < end and lst[j + 1] > lst[j]:
                    j += 1
                elif temp > lst[j]:
                    break
                else:
                    lst[i] = lst[j]
                    i, j = j, 2*j+1
            lst[i] = temp

        def heap_sort(lst):
            if not lst:
                return []
            end = len(lst)
            for i in range((end//2)-1, -1, -1):
                siftup(lst, lst[i], i, end)
            for i in range(end-1, 0, -1):
                temp = lst[i]
                lst[i] = lst[0]
                siftup(lst, temp, 0, i)
            return lst

        if not tinput or k > len(tinput):
            return []
        tinput = heap_sort(tinput)
        return tinput[:k]



























