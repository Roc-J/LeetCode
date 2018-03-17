# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        number1 = bin(n).replace('0b','')
        result = 0
        for item in number1:
            if item == '1':
                result += 1
        return result

if __name__ == '__main__':
    print Solution().hammingWeight(11)