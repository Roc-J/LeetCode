# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        while n > 1:
            r = n % 2
            if r > 0:
                return False
            n = n/2
        return True


if __name__ == '__main__':
    print Solution().isPowerOfTwo(6)

