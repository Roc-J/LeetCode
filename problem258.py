# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            count = 0
            for item in str(num):
                count += int(item)
            num = count
        return num

if __name__ == '__main__':
    print Solution().addDigits(38)