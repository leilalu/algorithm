"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5

示例1
输入
1,2,3,4,5,6,7,0
输出
7

"""


class Solution:
    def InversePairs(self, data):
        """"
        归并排序
        这道题可以这么想，我们要找到数组中的逆序对，可以看做对数据进行排序，需要交换数组中的元素的次数，
        但是防止相同大小的元素发生交换，因此需要选择一个稳定的排序方法，记录发生交换的次数。
        那么，基于比较的稳定的排序方法中，最快的方法就是归并了，
        所以直接按照归并排序的思路，将数组分解、合并、排序即可。

        但是需要注意的是，在常规归并排序的时候，如果前一个元素大于后一个元素，直接进行交换即可，只进行了一次操作，
        但是对于这道题来讲，对于每一次的归并段，我们选择从后向前遍历，前面的归并段的某一个数值left[i]如果大于后面的某一个数值right[j]，
        因为在right自己独自排序的过程中，已经保证了right是有序的，
        所以j位置前面的数字全部小于right[j]，所以在这里逆序对的个数就会是 j-start-length，其中start是整个数组的起点，length是left的长度，然后再进行交换。


        归并排序的时间复杂度是 O(nlogn) 同时需要一个长度为n的辅助数组
        空间复杂度O(n) 用空间换时间

        """
        length = len(data)
        if not data or length <= 0:
            return 0

        # 建立辅助数组
        copy = [0] * length
        for i in range(length):
            copy[i] = data[i]

        count = self.InversePairsCore(data, copy, 0, length-1)

        return count % 1000000007

    def InversePairsCore(self, data, copy, start, end):
        # 递归出口，划分为长度为1的子数组
        if start == end:
            copy[start] = data[start]
            return 0

        length = (end - start) // 2  # 每个子数组的长度

        # 每个子数组进行归并排序
        left = self.InversePairsCore(copy, data, start, start+length)
        right = self.InversePairsCore(copy, data, start+length+1, end)


        # 归并排序
        # i 初始化为前半段的最后一个数字的下标
        i = start + length
        # j 初始化为后半段的最后一个数字下标
        j = end

        indexCopy = end
        count = 0
        while i >= start and j >= start+length+1:
            if data[i] > data[j]:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j-start-length

            else:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1

        while i >= start:
            copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1

        while j >= start+length+1:
            copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1

        return left + right + count


if __name__ == '__main__':
    nums = [1,3,2,3,1]
    res = Solution().InversePairs(nums)
    print(res)


