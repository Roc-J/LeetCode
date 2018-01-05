#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if len(s) == 0 or s[0] == 'e':
            return False
        try:
            a = float(s)
            return True
        except:
            return False

if __name__ == '__main__':
    print(Solution().isNumber("2e10"))