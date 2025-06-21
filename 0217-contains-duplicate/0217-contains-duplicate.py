class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}

        for num in nums:
            if num in seen and seen[num] >=1:
                return True

            seen[num] = seen.get(num, 0) +1
        return False

        

