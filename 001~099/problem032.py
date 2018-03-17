#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0
        stack = 0
        max_ = [0]*len(s)
        maxlen = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack += 1
            elif s[i] == ')':
                if stack > 0:
                    stack -= 1
                    max_[i] = max_[i-1] + 2
                    if i - max_[i] >= 0 :
                        max_[i] += max_[i - max_[i]]
            maxlen = max(max_[i], maxlen)
        return maxlen


if __name__ == '__main__':
    print(Solution().longestValidParentheses("()(())"))

