# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def factn(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factn(n-1)

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += n/5
            n = n/5

        return count

if __name__ == '__main__':
    for i in range(51):
        print Solution().trailingZeroes(i)
        print Solution().factn(i)
        print '##'
