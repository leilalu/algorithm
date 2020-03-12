class Solution:
    def findContinuousSequence(self, target):
        if target < 3:
            return []

        small = 1
        big = 2
        curSum = small + big
        middle = (target + 1) // 2

        res = []
        while small < middle:
            if curSum == target:
                sequence = self.getSequence(small, big)
                res.append(sequence)

            while curSum > target and small < middle:
                curSum -= small
                small += 1

                if curSum == target:
                    sequence = self.getSequence(small, big)
                    res.append(sequence)

            big += 1
            curSum += big

        return res

    def getSequence(self, small, big):
        sequence = []
        for i in range(small, big+1):
            sequence.append(i)
        return sequence