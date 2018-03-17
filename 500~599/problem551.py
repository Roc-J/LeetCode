# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        countA = 0
        for i in range(len(s)):
            if s[i] == 'A':
                countA += 1
            if countA > 1:
                return False
        for i in range(len(s)-2):
            if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
                return False
        return True
