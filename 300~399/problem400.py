# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0, 9, 90, 900, 9000, 90000, 900000, 9000000, 90000000, 900000000]
        for i in range(len(count)):
            if n > count[i]*i:
                n = n - count[i]*i
            else:
                r = n % i
                index = n/i
                sum = 1
                while (i-1) > 0:
                    sum *= 10
                    i = i - 1
                sum = sum -1
                number = sum + index
                if r > 0:
                    number += 1
                    result = str(number)
                    return int(result[r-1])
                else:
                    result = str(number)
                    return int(result[-1])

if __name__ == '__main__':
    print Solution().findNthDigit(100000000)