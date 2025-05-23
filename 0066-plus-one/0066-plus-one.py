class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carry = 0
        i = len(digits) -1
        while i >= 0:
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
            i -= 1

        return [1]+digits
        