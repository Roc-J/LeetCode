# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for item in ransomNote:
            if item in magazine:
                magazine.remove(item)
            else:
                return False
        return True

if __name__ == '__main__':
    print Solution().canConstruct("aa", "aab")
