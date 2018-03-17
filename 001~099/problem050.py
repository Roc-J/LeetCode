# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n > 0:
            if n == 1:
                return x
            if n % 2 == 0:
                return self.myPow(x, n/2)*self.myPow(x, n/2)
            else:
                return x*self.myPow(x, (n-1)/2) * self.myPow(x, (n-1)/2)
        else:
            n = -n
            if n == 1:
                return 1.0/x
            if n % 2 == 0:
                return 1.0/(self.myPow(x, n/2)*self.myPow(x, n/2))
            else:
                return 1.0/(x*self.myPow(x, (n-1)/2) * self.myPow(x, (n-1)/2))

    def myPow(self, x, n):
        if n < 0:
            return 1.0 / self.power(x, -n)
        else:
            return self.power(x, n)

    def power(self, x, n):
        if n == 0:
            return 1

        tmp = self.power(x, n / 2)

        if n & 0x01 == 1:
            return tmp * tmp * x
        else:
            return tmp * tmp
if __name__ == '__main__':
    print Solution().myPow(8.95371, -1)