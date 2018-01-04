#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''
括号匹配
使用递归
１．　左括号比右括号多
２．　

'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(S='', left=0, right=0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)

        backtrack()
        return ans

if __name__ == '__main__':
    print(Solution().generateParenthesis(4))