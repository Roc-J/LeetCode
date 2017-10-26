# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        number1 = int(a, 2)
        number2 = int(b, 2)
        return str(bin(number1+number2).replace('0b', ''))

if __name__ == '__main__':
    print Solution().addBinary('11', '1')