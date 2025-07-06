class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans = []

        for i in range(len(nums)):
            x = abs(nums[i])
            idx = x-1

            #check if visited
            if nums[idx] < 0:
                ans.append(x)
            else:
                nums[idx] *= -1

        return ans
        