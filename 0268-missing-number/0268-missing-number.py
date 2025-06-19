class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        n = len(nums)
        for i in range(n+1):
            if i not in nums:
                return i"""

        n = len(nums)
        xor_all = 0  #0~n까지의숫자전체를 xor할 변수
        xor_nums = 0 # nums 배열에 있는 숫자들을 xor할 변수
        for i in range(n+1):
            xor_all ^= i

        for num in nums:
            xor_nums ^= num

        return xor_all ^ xor_nums

