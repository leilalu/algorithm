class Solution:
    def atoi(self, str):
        res = 0
        firstsign = True
        frontspace = True
        sign = 1

        for i in str:
            if i == ' ':
                if not frontspace:
                    break

            elif i == '-':
                if firstsign:
                    firstsign = False
                    frontspace = False
                    sign = -1
                else:
                    break

            elif i == '+':
                if firstsign:
                    firstsign = False
                    frontspace = False
                else:
                    break

            elif '0' <= i <= '9':
                firstsign = False
                frontspace = False
                res = res * 10 + ord(i) - ord('0')

            else:
                break

        res = res * sign
        if res < -2147483648:
            return -2147483648
        if res > 2147483647:
            return 2147483647

        return res
