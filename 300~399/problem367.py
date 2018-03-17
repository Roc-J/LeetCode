# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 1, num
        while low <= high:
            mid = (low + high)/2
            if mid * mid > num:
                high = mid - 1
            elif mid * mid == num:
                return True
            else:
                low = mid + 1
        return False

if __name__ == '__main__':
    for i in range(37):

        print Solution().isPerfectSquare(i)