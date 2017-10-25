# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        num2str = str(x)
        left = ''
        right = ''
        for item in num2str:
            left += item
        for item in num2str[::-1]:
            right += item

        if left == right:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().isPalindrome(-2147447412)