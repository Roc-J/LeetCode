# -*- coding:utf-8 -*-
# Author: Roc-J

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = ''
        for item in s:
            if item >='a' and item <='z':
                string += item
            elif item >='A' and item <= 'Z':
                string += item.lower()
            elif item >= '0' and item<= '9':
                string += item
            else:
                continue
        if len(string) <= 1:
            return True
        i = 0
        j = len(string) - 1
        while True:
            if string[i] != string[j]:
                break
            else:
                i += 1
                j -= 1
            if i >= j:
                break

        if i < j:
            return False
        else:
            return True

if __name__ == '__main__':
    print Solution().isPalindrome('ab'