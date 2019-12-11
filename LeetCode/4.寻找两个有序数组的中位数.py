def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)

    cur1 = 0
    cur2 = 0

    new_list = []

    while (cur1 < m) and (cur2 < n):
        if nums1[cur1] < nums2[cur2]:
            new_list.append(nums1[cur1])
            cur1 += 1
        elif nums1[cur1] > nums2[cur2]:
            new_list.append(nums2[cur2])
            cur2 += 1
        else:
            new_list.append(nums1[cur1])
            new_list.append(nums2[cur2])
            cur1 += 1
            cur2 += 1

    if cur1 != m:
        for i in range(cur1, m):
            new_list.append(nums1[i])

    if cur2 != n :
        for i in range(cur2, n):
            new_list.append(nums2[i])

    if (m + n) % 2 == 0:
        a = int((m + n) // 2 - 1)
        b = int((m + n) // 2)
        print(a,b)
        print(new_list[a])

        medium = (new_list[a] + new_list[b]) / 2
        return medium
    else:
        return new_list[int((m + n) // 2)]


nums1 = [1,2]
nums2 = [3,4]

res = findMedianSortedArrays(nums1, nums2)