class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        

        set_nums = set(nums)
        result =[]
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                result.append(i)
        return result
        """
        i=0
        result =[]

        while i < len(nums):
            while nums[i] != nums[nums[i] -1]:
                nums[nums[i] -1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i+=1

        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(i+1)
        return result
