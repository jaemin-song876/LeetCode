class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right: #이진탐색 시작
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid <x:
                left = mid + 1
            else:
                right = mid - 1
        return right #right는 마지막으로 mid*mid가 x보다 작거나 같았던 숫자임