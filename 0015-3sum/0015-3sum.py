class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        results = []
        nums.sort()

        for i in range(len(nums) - 2): #첫번째 수 고르기
            if i>0 and nums[i] == nums[i - 1]:
                continue #no repeat

            left, right = i+1, len(nums)-1 #두번째 세번째 수를 위한 투포인터

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total >0:
                    right -=1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                #remove duplicate when answer found
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left +=1
                    right -=1
        return results



