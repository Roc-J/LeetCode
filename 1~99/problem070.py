# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        result = [1, 2]
        for i in range(2, n):
            result.append(result[i-1] + result[i-2])

        return result[n-1]

if __name__ == '__main__':
    print Solution().climbStairs(35)