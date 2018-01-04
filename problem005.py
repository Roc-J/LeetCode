#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: qjk

'''

还是遍历，不过要考虑是偶数还是奇数两种情况
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def palindrome(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        ans = ''

        for i in range(len(s)):
            pal1 = palindrome(s, i, i)
            if len(pal1) > len(ans):
                ans = pal1
            pal2 = palindrome(s, i, i + 1)
            if len(pal2) > len(ans):
                ans = pal2

        return ans

if __name__ == '__main__':
    print(Solution().longestPalindrome("aabaaa"))
