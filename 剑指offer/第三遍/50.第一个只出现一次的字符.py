class Solution:
    def firstUniqChar(self, s):
        if not s or len(s) <= 0:
            return ' '

        char_count = [0] * 256
        for item in s:
            char_count[ord(item)] += 1

        for item in s:
            if char_count[ord(item)] == 1:
                return item

        return ' '
