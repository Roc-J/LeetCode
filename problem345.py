# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        number1 = []
        number2 = []
        for item in s:
            if item in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
                number1.append(item)
            else:
                number2.append(item)

        for i in range(len(s)):
            if s[i] in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
                number2.insert(i, number1.pop())

        return ''.join(number2)
if __name__ == '__main__':
    print Solution().reverseVowels("leetcode")