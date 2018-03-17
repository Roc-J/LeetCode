class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        flag1 = 0
        flag2 = 0
        for item in moves:
            if item == 'U':
                flag1 += 1
            elif item == 'D':
                flag1 = flag1 - 1
            elif item == 'L':
                flag2 += 1
            else:
                flag2 = flag2 - 1

        if flag1 == 0 and flag2 == 0:
            return True
        else:
            return False
