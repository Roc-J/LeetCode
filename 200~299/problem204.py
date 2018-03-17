# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def prime(self, n):
        if n == 2:
            return True
        if n == 3:
            return True
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                if i < int(math.sqrt(n))+1:
                    return False
                else:
                    return True
        return True


    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        count = 0
        for i in range(2, n):
            if self.prime(i) == True:
                count += 1
        return count




if __name__ == '__main__':
    print Solution().countPrimes(999983)