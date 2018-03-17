# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

if __name__ == '__main__':
    print Solution().countSegments("")