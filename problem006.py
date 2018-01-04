#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = []
        for i in range(numRows):
            flag = 1
            step = (numRows - 1) * 2
            step1 = (numRows - i - 1) * 2
            step2 = step - step1
            if i == 0 or i == numRows-1:
                j = i
                while j < len(s):
                    result.append(s[j])
                    j += step
            else:
                j = i
                while j < len(s):
                    result.append(s[j])
                    if flag == 1:
                        j += step1
                        flag = 0
                    else:
                        j += step2
                        flag = 1
        return "".join(result)

if __name__ == '__main__':
    print(Solution().convert("ABc", 2))