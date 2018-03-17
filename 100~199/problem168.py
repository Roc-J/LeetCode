# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ''
        while n > 0:
            r = (n-1) % 26
            result = chr(ord('A') + r) + result
            n = (n-1)/26
        return result


if __name__ == '__main__':
    print Solution().convertToTitle(520)