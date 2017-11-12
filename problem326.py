# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0:
            return False
        if n == 1:
            return True
        if n == 0 or n%3 >0:
            return False

        while n > 1:
            r = n % 3
            if r > 0:
                return False
            n = n/3
        return True

if __name__ == '__main__':
    print Solution().isPowerOfThree(9)