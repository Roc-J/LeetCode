# -*- coding:utf-8 -*- 
# Author: Roc-J

class Solution(object):
    def plusOne1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''
        L = list()
        for i in range(len(digits)):
            string += str(digits[i])
        number = int(string) + 1
        for i in str(number):
            L.append(int(i))

        return L

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        c = 0
        if length > 0:
            if digits[length-1] + 1 < 10:
                digits[length-1] += 1
                return digits
            else:
                c = 1
                digits[length-1] = 0
                length -= 1

        while length:
            if digits[length-1] + c < 10:
                digits[length-1] = digits[length-1] + c
                return digits
            else:
                digits[length - 1] = 0
                length -= 1
        if c == 1:
            digits.insert(0, c)

        return digits

if __name__ == '__main__':
    print Solution().plusOne([0])


