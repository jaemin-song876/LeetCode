class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #linear runtime complexity여서
        #딕셔너리 말고 xor연산 써야함.

        result=0
        for num in nums:
            result ^= num
        return result
        
        