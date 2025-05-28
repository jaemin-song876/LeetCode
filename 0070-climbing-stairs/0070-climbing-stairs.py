import math
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n==0 or n==1:# 0칸이나 1칸은 딱한가지
            return 1
        prev, curr =1,1
        #prev = f(n-2) 두칸아래
        #curr = f(n-1) 한칸아래

        for i in range(2, n+1):
            temp = curr
            curr = prev + curr # 앞의 두 수를 더해서 다음수 만들기
            prev = temp
        return curr
        