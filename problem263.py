# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        while num > 1:
            r = num % 2
            if r > 0:
                r = num % 3
                if r > 0:
                    r = num % 5
                    if r > 0:
                        return False
                    else:
                        num = num/5
                else:
                    num = num/3
            else:
                num = num/2
        return True

if __name__ == '__main__':
    print Solution().isUgly(14)