class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write =0
        for read in range(0, len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write +=1
        return write

