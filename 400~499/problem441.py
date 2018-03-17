# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        while n >= count:
            if n - count >= 0:
                n = n - count
                count += 1
        return count-1

if __name__ == '__main__':
    for i in range(11):
        print Solution().arrangeCoins(i)