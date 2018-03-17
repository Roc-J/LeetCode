# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def countn(self, n):
        sum = 0
        while n:
            r = n % 10
            sum += r*r
            n = int(n/10)
        return sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        number = list()
        num = self.countn(n)
        while True:
            if num == 1:
                return True
            elif num in number:
                return False
            else:
                number.append(num)
                num = self.countn(num)

if __name__ == '__main__':
    print Solution().isHappy(33)