# -*- coding:utf-8 -*- 
# Author: Roc-J
'''

32位有符号整数范围
-2^32 - 2^32
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -x
            flag = 1
        else:
            flag = 0
        num2str = str(x)
        result = ''
        for item in num2str[::-1]:
            result += item
        result = int(result)
        number = result

        n = 31
        while n:
            result = result * 1.0/2
            n = n - 1
        if result > 1:
            return 0

        if flag == 1:
            number = -number
        return number

if __name__ == '__main__':
    print Solution().reverse(8463847412)