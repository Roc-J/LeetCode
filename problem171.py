# -*- coding:utf-8 -*- 
# Author: Roc-J
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        flag = 1
        result = 0
        for item in s[::-1]:
            result = (ord(item)-ord('A') + 1) * flag + result
            flag = flag * 26
        return result

if __name__ == '__main__':
    print Solution().titleToNumber('BAA')