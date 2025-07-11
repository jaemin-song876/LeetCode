class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set=set(nums)
        longest = 0

        for num in num_set:
            if not num-1 in num_set :
                starting_point = num
                length = 1
                while starting_point + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest